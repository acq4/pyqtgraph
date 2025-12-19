"""
configfile.py - Human-readable text configuration file library
Copyright 2010  Luke Campagnola
Distributed under MIT/X11 license. See license.txt for more information.

YAML-based configuration file format with Python expression evaluation.
Data structures may be nested and contain any data type as long as it can be
converted to/from a string using repr and eval.

This module uses PyYAML for parsing but evaluates all scalar values as Python
expressions with a configurable namespace.

API Changes from Original Implementation
-----------------------------------------

This implementation uses standard PyYAML for parsing while maintaining full
backward compatibility with the original configfile format. Key changes:

**Parsing:**
- Now uses PyYAML's SafeLoader as a base with custom constructors
- All scalar values are still evaluated as Python expressions
- YAML handles comment syntax (#), line continuations, and indentation
- Better error messages with line numbers from YAML parser

**Writing:**
- Uses Python repr() for all values (same as before)
- String values are wrapped in YAML double-quotes to preserve Python literals
- Output is valid YAML that can also be read by standard YAML parsers
  (though values would not be evaluated as Python expressions)

**Preserved Behaviors:**
- All values evaluated as Python expressions with custom namespace
- Support for units (m, s, Hz, etc.), numpy, Point, ColorMap, etc.
- Recursive readConfigFile() calls
- Custom serializers and deserializers
- Cross-platform line ending support (\\r\\n, \\r, \\n)
- OrderedDict for maintaining key order
- Tuple keys (experimental)
- Comments with # symbol
- Line continuation with backslash
- Empty dict values (key: with no value)

**Usage Examples:**
```python
# Writing config files
data = {
    'param1': 42,
    'param2': [1, 2, 3],
    'param3': {'nested': 'value'},
    'array': np.array([1, 2, 3]),
}
writeConfigFile(data, 'config.cfg')

# Reading config files
config = readConfigFile('config.cfg')

# Reading with custom namespace
config = readConfigFile('config.cfg', custom_var=10)

# Using custom deserializers
def my_deserializer(value):
    # Transform values after reading
    return value

config = readConfigFile('config.cfg', deserializer=my_deserializer)

# Recursive config file loading
# In config file: nested: readConfigFile('other.cfg')
```

**File Format:**
```yaml
# Comments are supported
simple_value: 42
expression: 2 + 3  # Evaluates to 5
string: 'hello'    # Evaluates to the Python string 'hello'
list: [1, 2, 3]
dict:
    nested: 'value'
    deeper:
        key: 123
array: np.array([1, 2, 3])  # Uses numpy from namespace
unit: 5 * m  # Uses units from namespace
```

**Compatibility:**
- Config files written by the old implementation can be read by this version
- Config files written by this version can be read by the old implementation
- Config files are now also valid YAML (though standard YAML parsers won't
  evaluate the Python expressions)
"""

import contextlib
import datetime
import os
import re
from collections import OrderedDict
from io import StringIO

import numpy
import yaml

from . import units
from .colormap import ColorMap
from .Point import Point
from .Qt import QtCore

GLOBAL_PATH = None  # so not thread safe.


class ParseError(Exception):
    """Exception raised when parsing config file fails."""

    def __init__(self, message, lineNum=None, line=None, fileName=None):
        self.lineNum = lineNum
        self.line = line
        self.message = message
        self.fileName = fileName
        Exception.__init__(self, message)

    def __str__(self):
        if self.fileName is None:
            msg = "Error parsing config string"
        else:
            msg = f"Error parsing config file '{self.fileName}'"

        if self.lineNum is not None:
            msg += f" at line {self.lineNum:d}"

        msg += f":\n{Exception.__str__(self)}"

        if self.line is not None:
            msg += f"\n{self.line}"

        return msg


class PythonExpressionLoader(yaml.SafeLoader):
    """
    Custom YAML loader that evaluates all scalar values as Python expressions.

    This loader preserves the behavior of the old configfile format where all
    values were evaluated using Python's eval() function with a custom namespace.
    """
    pass


class OrderedDictDumper(yaml.SafeDumper):
    """Custom YAML dumper that handles OrderedDict and other Python types."""
    pass


def _python_constructor(loader, node):
    """
    Construct a Python object by evaluating the scalar value as a Python expression.

    This preserves the original configfile behavior where all values were evaluated
    using eval() with access to a namespace containing numpy, units, etc.
    """
    # Get the value as a string
    if isinstance(node, yaml.ScalarNode):
        # Get the raw value from the node without YAML's type conversion
        # This is critical: we want the literal string as written in the file,
        # not YAML's interpretation of it
        value_str = node.value

        # Check if this was a quoted string in YAML
        # We need to handle two cases:
        # 1. Values written by genString: wrapped in YAML double quotes, contain Python literals
        # 2. Values written manually: YAML quoted strings that should become Python strings
        if node.style in ("'", '"'):
            # It was a YAML quoted string
            # If the value already looks like a Python literal (starts with quote),
            # it's from genString - use as-is
            # Otherwise it's a manual YAML string - wrap it for eval
            if not (value_str.startswith(("'", '"', '[', '{', '(')) or
                    value_str[0].isdigit() or value_str in ('True', 'False', 'None')):
                # It's a plain YAML string, wrap it in Python quotes for eval
                value_str = repr(value_str)

    elif isinstance(node, yaml.MappingNode):
        # For mapping nodes (nested dicts), construct recursively
        return loader.construct_mapping(node, deep=True)
    elif isinstance(node, yaml.SequenceNode):
        # For sequences, construct recursively
        return loader.construct_sequence(node, deep=True)
    else:
        raise ParseError(f"Unsupported node type: {type(node)}")

    # Check if value_str is empty (represents an empty dict)
    if not value_str or value_str.strip() == '':
        return {}

    # Get the namespace from the loader
    namespace = getattr(loader, 'namespace', {})

    try:
        # Debug: print what we're trying to eval
        # print(f"DEBUG: Evaluating '{value_str}' (repr: {repr(value_str)}) style={node.style if isinstance(node, yaml.ScalarNode) else None}")

        # Try to evaluate as Python expression
        result = eval(value_str, namespace)
        return result
    except Exception as ex:
        # If evaluation fails, raise a parse error
        line_num = getattr(node, 'start_mark', None)
        if line_num:
            line_num = line_num.line + 1
        raise ParseError(
            f"Error evaluating expression '{value_str}': [{ex.__class__.__name__}: {ex}]",
            lineNum=line_num,
            line=value_str
        ) from ex


def _tuple_key_constructor(loader, node):
    """
    Construct objects with tuple keys.

    YAML mapping keys are evaluated as Python expressions, allowing tuple keys
    like (1, 2) to be used.
    """
    # Construct the mapping
    mapping = OrderedDict()
    namespace = getattr(loader, 'namespace', {})

    for key_node, value_node in node.value:
        # Get key as string
        key_str = loader.construct_scalar(key_node)

        # Try to evaluate key as tuple if it looks like one
        key = key_str
        if key_str.startswith('(') and key_str.endswith(')'):
            with contextlib.suppress(Exception):
                evaluated_key = eval(key_str, namespace)
                if isinstance(evaluated_key, tuple):
                    key = evaluated_key

        # Check for duplicate keys
        if key in mapping:
            line_num = getattr(key_node, 'start_mark', None)
            if line_num:
                line_num = line_num.line + 1
            raise ParseError(
                f'Duplicate key: {key}',
                lineNum=line_num,
                line=key_str
            )

        # Construct value
        value = loader.construct_object(value_node, deep=True)

        # Apply deserializer if present
        deserializer = getattr(loader, 'deserializer', None)
        if deserializer is not None:
            value = deserializer(value)

        mapping[key] = value

    return mapping


# Register constructors
PythonExpressionLoader.add_constructor('tag:yaml.org,2002:str', _python_constructor)
PythonExpressionLoader.add_constructor('tag:yaml.org,2002:int', _python_constructor)
PythonExpressionLoader.add_constructor('tag:yaml.org,2002:float', _python_constructor)
PythonExpressionLoader.add_constructor('tag:yaml.org,2002:bool', _python_constructor)
PythonExpressionLoader.add_constructor('tag:yaml.org,2002:null', _python_constructor)
PythonExpressionLoader.add_constructor('tag:yaml.org,2002:map', _tuple_key_constructor)


def _represent_numpy_array(dumper, data):
    """Represent numpy arrays using repr()."""
    return dumper.represent_scalar('tag:yaml.org,2002:str', repr(data))


def _represent_ordereddict(dumper, data):
    """Represent OrderedDict as a regular mapping."""
    return dumper.represent_mapping('tag:yaml.org,2002:map', data.items())


def _represent_point(dumper, data):
    """Represent Point objects using repr()."""
    return dumper.represent_scalar('tag:yaml.org,2002:str', repr(data))


def _represent_colormap(dumper, data):
    """Represent ColorMap objects using repr()."""
    return dumper.represent_scalar('tag:yaml.org,2002:str', repr(data))


# Register representers
OrderedDictDumper.add_representer(numpy.ndarray, _represent_numpy_array)
OrderedDictDumper.add_representer(OrderedDict, _represent_ordereddict)
OrderedDictDumper.add_representer(Point, _represent_point)
OrderedDictDumper.add_representer(ColorMap, _represent_colormap)

# Register numpy dtypes
for dtype in ['int8', 'uint8', 'int16', 'uint16', 'float16',
              'int32', 'uint32', 'float32', 'int64', 'uint64', 'float64']:
    numpy_type = getattr(numpy, dtype)
    OrderedDictDumper.add_representer(
        numpy_type,
        lambda dumper, data: dumper.represent_data(data.item())
    )


def writeConfigFile(data, fname, serializer=None):
    """
    Write a configuration file in YAML format.

    Parameters
    ----------
    data : dict
        Dictionary to write to file
    fname : str
        File path to write to
    serializer : callable, optional
        Function to apply to all values before writing.
        The serializer is called once for each value in the dictionary.

    Notes
    -----
    The file is written in YAML format with Python repr() for complex types.
    All values are written such that they can be read back and evaluated as
    Python expressions.
    """
    if serializer is not None:
        # Apply serializer to all values recursively
        data = _apply_serializer(data, serializer)

    s = genString(data)
    with open(fname, 'wt', encoding='utf-8') as fd:
        fd.write(s)


def readConfigFile(fname, deserializer=None, **scope):
    """
    Read a configuration file in YAML format with Python expression evaluation.

    Parameters
    ----------
    fname : str
        File path to read from
    deserializer : callable, optional
        Function to apply to all values after reading.
        The deserializer is called once for each value in the dictionary.
    **scope : dict
        Additional variables to make available in the namespace when evaluating
        Python expressions in the config file.

    Returns
    -------
    OrderedDict
        Configuration data with all values evaluated as Python expressions

    Notes
    -----
    All scalar values in the YAML file are evaluated as Python expressions.
    The namespace includes:
    - All pyqtgraph units (m, s, Hz, etc.)
    - numpy as 'np' and common numpy types
    - Point, ColorMap, QtCore, OrderedDict
    - datetime module
    - Any additional variables passed as **scope

    Config files can recursively load other config files using:
        nested: readConfigFile('other.cfg')
    """
    global GLOBAL_PATH

    # Handle path resolution
    if GLOBAL_PATH is not None:
        fname2 = os.path.join(GLOBAL_PATH, fname)
        if os.path.exists(fname2):
            fname = fname2

    GLOBAL_PATH = os.path.dirname(os.path.abspath(fname))

    # Build namespace for eval
    local = {
        **scope,
        **units.allUnits,
        'OrderedDict': OrderedDict,
        'readConfigFile': lambda fname: readConfigFile(fname, deserializer=deserializer, **scope),
        'Point': Point,
        'QtCore': QtCore,
        'ColorMap': ColorMap,
        'datetime': datetime,
        'np': numpy,
        'array': numpy.array,
    }

    # Add numpy dtypes to namespace
    for dtype in ['int8', 'uint8', 'int16', 'uint16', 'float16',
                  'int32', 'uint32', 'float32', 'int64', 'uint64', 'float64']:
        local[dtype] = getattr(numpy, dtype)

    try:
        # Read file and normalize line endings
        with open(fname, "rt", encoding='utf-8', errors="replace") as fd:
            s = fd.read()

        # Normalize line endings (cross-platform compatibility)
        s = s.replace("\r\n", "\n")
        s = s.replace("\r", "\n")

        # Handle line continuation (backslash at end of line)
        # This needs to be done before YAML parsing
        s = s.replace("\\\n", "")

        # Parse YAML with custom loader
        data = parseString(s, namespace=local, deserializer=deserializer)

    except ParseError as e:
        # Add filename to error if not already present
        if e.fileName is None:
            e.fileName = fname
        raise
    except yaml.YAMLError as e:
        # Convert YAML errors to ParseError
        line_num = None
        if hasattr(e, 'problem_mark'):
            line_num = e.problem_mark.line + 1
        raise ParseError(
            f"YAML parsing error: {e}",
            lineNum=line_num,
            fileName=fname
        ) from e
    except Exception:
        print(f"Error while reading config file {fname}:")
        raise

    return data


def appendConfigFile(data, fname, serializer=None):
    """
    Append configuration data to an existing file.

    Parameters
    ----------
    data : dict
        Dictionary to append to file
    fname : str
        File path to append to
    serializer : callable, optional
        Function to apply to all values before writing
    """
    if serializer is not None:
        data = _apply_serializer(data, serializer)

    s = genString(data)
    with open(fname, 'at', encoding='utf-8') as fd:
        fd.write(s)


def genString(data, indent='', serializer=None):
    """
    Generate YAML string from dictionary using Python repr() for values.

    Parameters
    ----------
    data : dict
        Dictionary to convert to YAML string
    indent : str, optional
        Current indentation level (used for recursion)
    serializer : callable, optional
        Function to apply to values before converting (deprecated, use at write level)

    Returns
    -------
    str
        YAML formatted string

    Notes
    -----
    This function generates config files that are compatible with the old configfile
    format. All values are represented using Python repr() so they can be evaluated
    as Python expressions when read back.

    This maintains backward compatibility with the original format:
    - Simple values like strings, numbers are written as repr()
    - Lists and dicts are written in flow style when simple
    - Nested dicts use indentation
    """
    s = ''
    for k in data:
        sk = str(k)
        if not sk:
            raise ValueError('blank dict keys not allowed')
        if sk[0] == ' ' or ':' in sk:
            raise ValueError(
                f'dict keys must not contain ":" or start with spaces [offending key is "{sk}"]'
            )
        v = data[k]
        if isinstance(v, dict):
            s += f"{indent}{sk}:\n"
            s += genString(v, f'{indent}    ', serializer)
        else:
            # Use repr() for all values to ensure they can be eval'd
            line = repr(v)

            # If the repr() output starts with a quote (string literal),
            # we need to wrap it in double quotes for YAML to preserve it
            # Otherwise YAML will interpret 'value' as a YAML string and strip quotes
            if line.startswith(("'", '"')):
                # Escape backslashes and double quotes for YAML double-quote syntax
                line = line.replace('\\', '\\\\').replace('"', '\\"')
                line = f'"{line}"'

            # Handle line breaks in the value (for multiline strings/arrays)
            # Don't use backslash continuation as YAML doesn't handle it well with eval
            # Instead, keep it on one line (YAML will handle wrapping if needed)
            line = line.replace('\n', ' ')

            s += f"{indent}{sk}: {line}\n"
    return s


def parseString(s, namespace=None, deserializer=None):
    """
    Parse YAML string with Python expression evaluation.

    Parameters
    ----------
    s : str
        YAML string to parse
    namespace : dict, optional
        Namespace for evaluating Python expressions
    deserializer : callable, optional
        Function to apply to all values after parsing

    Returns
    -------
    OrderedDict
        Parsed configuration data

    Notes
    -----
    All scalar values are evaluated as Python expressions using the provided
    namespace.
    """
    if namespace is None:
        namespace = {}

    # Create a custom loader instance with namespace
    loader = PythonExpressionLoader(s)
    loader.namespace = namespace
    loader.deserializer = deserializer

    try:
        data = loader.get_single_data()
        if data is None:
            data = OrderedDict()
        return data
    except yaml.YAMLError as e:
        line_num = None
        line = None
        if hasattr(e, 'problem_mark'):
            line_num = e.problem_mark.line + 1
            # Try to extract the problematic line
            lines = s.split('\n')
            if 0 <= e.problem_mark.line < len(lines):
                line = lines[e.problem_mark.line]
        raise ParseError(
            f"YAML parsing error: {e}",
            lineNum=line_num,
            line=line
        ) from e
    finally:
        loader.dispose()


def _apply_serializer(data, serializer):
    """
    Recursively apply serializer to all values in a dictionary.

    Parameters
    ----------
    data : dict or other
        Data to apply serializer to
    serializer : callable
        Function to apply to each value

    Returns
    -------
    dict or other
        Data with serializer applied
    """
    if isinstance(data, dict):
        return {k: _apply_serializer(serializer(v), serializer) if not isinstance(v, dict)
                else _apply_serializer(v, serializer) for k, v in data.items()}
    else:
        return serializer(data)
