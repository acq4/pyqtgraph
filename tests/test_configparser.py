import numpy as np
import pytest
from collections import OrderedDict

from pyqtgraph import configfile
from pyqtgraph import Point, units
from pyqtgraph.colormap import ColorMap


def test_longArrays(tmpdir):
    """
    Test config saving and loading of long arrays.
    """
    arr = np.arange(20)

    tf = tmpdir.join("config.cfg")
    configfile.writeConfigFile({'arr': arr}, tf)
    config = configfile.readConfigFile(tf)
    assert all(config['arr'] == arr)


def test_multipleParameters(tmpdir):
    """
    Test config saving and loading of multiple parameters.
    """

    par1 = [1,2,3]
    par2 = "Test"
    par3 = {'a':3,'b':'c'}

    tf = tmpdir.join("config.cfg")
    configfile.writeConfigFile({'par1':par1, 'par2':par2, 'par3':par3}, tf)
    config = configfile.readConfigFile(tf)

    assert config['par1'] == par1
    assert config['par2'] == par2
    assert config['par3'] == par3


def test_duplicate_keys_error(tmpdir):
    """
    Test that an error is raised when duplicate keys are present in the config file.
    """

    tf = tmpdir.join("config.cfg")
    with open(tf, 'w') as f:
        f.write('a: 1\n')
        f.write('a: 2\n')

    try:
        configfile.readConfigFile(tf)
    except configfile.ParseError as e:
        assert 'Duplicate key' in str(e)
    else:
        assert False, "Expected ParseError"


def test_line_numbers_acconut_for_comments_and_blanks(tmpdir):
    """
    Test that line numbers in ParseError account for comments and blank lines.
    """

    tf = tmpdir.join("config.cfg")
    with open(tf, 'w') as f:
        f.write('a: 1\n')
        f.write('\n')
        f.write('# comment\n')
        f.write('a: 2\n')

    try:
        configfile.readConfigFile(tf)
    except configfile.ParseError as e:
        assert 'at line 4' in str(e)
    else:
        assert False, "Expected ParseError"


def test_comment_indentation_is_ignored(tmpdir):
    """
    Test that comment indentation is ignored.
    """

    tf = tmpdir.join("config.cfg")
    with open(tf, 'w') as f:
        f.write('a:\n')
        f.write('        # comment\n')
        f.write('    b:\n')
        f.write('# more comments\n')
        f.write('        c: 2\n')

    retval = configfile.readConfigFile(tf)
    assert retval['a']['b']['c'] == 2


def test_eval_python_expressions(tmpdir):
    """
    Test that values are evaluated as Python expressions.
    """
    tf = tmpdir.join("config.cfg")
    with open(tf, 'w') as f:
        f.write('a: 1 + 2\n')
        f.write('b: [1, 2, 3]\n')
        f.write('c: {"x": 10, "y": 20}\n')
        f.write('d: (1, 2, 3)\n')
        f.write('e: True\n')
        f.write('f: None\n')

    config = configfile.readConfigFile(tf)
    assert config['a'] == 3
    assert config['b'] == [1, 2, 3]
    assert config['c'] == {"x": 10, "y": 20}
    assert config['d'] == (1, 2, 3)
    assert config['e'] is True
    assert config['f'] is None


def test_cross_platform_line_endings(tmpdir):
    """
    Test that different line endings are handled correctly.
    """
    tf = tmpdir.join("config.cfg")
    # Write with Windows line endings
    with open(tf, 'wb') as f:
        f.write(b'a: 1\r\n')
        f.write(b'b: 2\r\n')

    config = configfile.readConfigFile(tf)
    assert config['a'] == 1
    assert config['b'] == 2

    # Write with old Mac line endings
    with open(tf, 'wb') as f:
        f.write(b'a: 3\r')
        f.write(b'b: 4\r')

    config = configfile.readConfigFile(tf)
    assert config['a'] == 3
    assert config['b'] == 4


def test_recursive_readConfigFile(tmpdir):
    """
    Test that config files can recursively load other config files.
    """
    # Create a nested config file
    nested_tf = tmpdir.join("nested.cfg")
    with open(nested_tf, 'w') as f:
        f.write('nested_value: 42\n')

    # Create main config file that loads the nested one
    main_tf = tmpdir.join("main.cfg")
    with open(main_tf, 'w') as f:
        f.write('main_value: 10\n')
        f.write(f'nested: readConfigFile("nested.cfg")\n')

    config = configfile.readConfigFile(main_tf)
    assert config['main_value'] == 10
    assert config['nested']['nested_value'] == 42


def test_custom_deserializer(tmpdir):
    """
    Test that custom deserializers work.
    """
    tf = tmpdir.join("config.cfg")
    with open(tf, 'w') as f:
        f.write('a: 10\n')
        f.write('b: 20\n')

    # Deserializer that multiplies all integers by 2
    def deserializer(val):
        if isinstance(val, int):
            return val * 2
        return val

    config = configfile.readConfigFile(tf, deserializer=deserializer)
    assert config['a'] == 20
    assert config['b'] == 40


def test_custom_serializer(tmpdir):
    """
    Test that custom serializers work.
    """
    tf = tmpdir.join("config.cfg")

    # Serializer that converts lists to tuples
    def serializer(val):
        if isinstance(val, list):
            return tuple(val)
        return val

    data = {'a': [1, 2, 3], 'b': 'test'}
    configfile.writeConfigFile(data, tf, serializer=serializer)

    # Read back and verify
    config = configfile.readConfigFile(tf)
    assert config['a'] == (1, 2, 3)  # List was serialized as tuple
    assert config['b'] == 'test'


def test_namespace_units(tmpdir):
    """
    Test that units from pyqtgraph.units are available in the namespace.
    """
    tf = tmpdir.join("config.cfg")
    with open(tf, 'w') as f:
        f.write('distance: 5 * m\n')
        f.write('time: 10 * s\n')

    config = configfile.readConfigFile(tf)
    # These should evaluate using the units namespace
    assert config['distance'] == 5 * units.m
    assert config['time'] == 10 * units.s


def test_namespace_numpy(tmpdir):
    """
    Test that numpy is available in the namespace.
    """
    tf = tmpdir.join("config.cfg")
    with open(tf, 'w') as f:
        f.write('arr: np.array([1, 2, 3])\n')
        f.write('zeros: np.zeros(5)\n')

    config = configfile.readConfigFile(tf)
    assert np.array_equal(config['arr'], np.array([1, 2, 3]))
    assert np.array_equal(config['zeros'], np.zeros(5))


def test_namespace_point(tmpdir):
    """
    Test that Point is available in the namespace.
    """
    tf = tmpdir.join("config.cfg")
    with open(tf, 'w') as f:
        f.write('point: Point(10, 20)\n')

    config = configfile.readConfigFile(tf)
    assert isinstance(config['point'], Point)
    assert config['point'].x() == 10
    assert config['point'].y() == 20


def test_namespace_colormap(tmpdir):
    """
    Test that ColorMap is available in the namespace.
    """
    tf = tmpdir.join("config.cfg")
    with open(tf, 'w') as f:
        f.write('cmap: ColorMap([0, 1], [(0, 0, 0), (255, 255, 255)])\n')

    config = configfile.readConfigFile(tf)
    assert isinstance(config['cmap'], ColorMap)


def test_ordered_dict(tmpdir):
    """
    Test that the returned config maintains order (OrderedDict).
    """
    tf = tmpdir.join("config.cfg")
    with open(tf, 'w') as f:
        f.write('z: 1\n')
        f.write('y: 2\n')
        f.write('x: 3\n')
        f.write('w: 4\n')

    config = configfile.readConfigFile(tf)
    assert isinstance(config, OrderedDict) or isinstance(config, dict)
    # Check that order is preserved
    keys = list(config.keys())
    assert keys == ['z', 'y', 'x', 'w']


def test_nested_dictionaries(tmpdir):
    """
    Test that nested dictionaries work correctly.
    """
    tf = tmpdir.join("config.cfg")
    with open(tf, 'w') as f:
        f.write('level1:\n')
        f.write('    level2:\n')
        f.write('        level3:\n')
        f.write('            value: 42\n')

    config = configfile.readConfigFile(tf)
    assert config['level1']['level2']['level3']['value'] == 42


def test_line_continuation(tmpdir):
    """
    Test that line continuation with backslash works.
    """
    tf = tmpdir.join("config.cfg")
    with open(tf, 'w') as f:
        f.write('long_list: [1, 2, 3, \\\n')
        f.write('           4, 5, 6]\n')

    config = configfile.readConfigFile(tf)
    assert config['long_list'] == [1, 2, 3, 4, 5, 6]


def test_tuple_keys(tmpdir):
    """
    Test that tuple keys are supported.
    """
    tf = tmpdir.join("config.cfg")
    with open(tf, 'w') as f:
        f.write('(1, 2): "tuple key"\n')
        f.write('normal: "string key"\n')

    config = configfile.readConfigFile(tf)
    assert config[(1, 2)] == "tuple key"
    assert config['normal'] == "string key"


def test_custom_scope_variables(tmpdir):
    """
    Test that custom scope variables are passed through.
    """
    tf = tmpdir.join("config.cfg")
    with open(tf, 'w') as f:
        f.write('a: custom_var * 2\n')
        f.write('b: custom_func(5)\n')

    config = configfile.readConfigFile(tf, custom_var=10, custom_func=lambda x: x ** 2)
    assert config['a'] == 20
    assert config['b'] == 25


def test_appendConfigFile(tmpdir):
    """
    Test that appendConfigFile works correctly.
    """
    tf = tmpdir.join("config.cfg")

    # Write initial data
    configfile.writeConfigFile({'a': 1, 'b': 2}, tf)

    # Append more data
    configfile.appendConfigFile({'c': 3, 'd': 4}, tf)

    # Read back
    config = configfile.readConfigFile(tf)
    assert config['a'] == 1
    assert config['b'] == 2
    assert config['c'] == 3
    assert config['d'] == 4


def test_empty_dict_value(tmpdir):
    """
    Test that empty dictionaries are handled correctly.
    """
    tf = tmpdir.join("config.cfg")
    with open(tf, 'w') as f:
        f.write('empty:\n')
        f.write('nonempty:\n')
        f.write('    value: 1\n')

    config = configfile.readConfigFile(tf)
    assert config['empty'] == {}
    assert config['nonempty']['value'] == 1


def test_string_values(tmpdir):
    """
    Test that string values work correctly.
    """
    tf = tmpdir.join("config.cfg")
    with open(tf, 'w') as f:
        f.write('single_quoted: \'hello\'\n')
        f.write('double_quoted: "world"\n')
        f.write('multiline: "line1\\nline2"\n')

    config = configfile.readConfigFile(tf)
    assert config['single_quoted'] == 'hello'
    assert config['double_quoted'] == 'world'
    assert config['multiline'] == 'line1\nline2'


def test_write_preserves_data_types(tmpdir):
    """
    Test that writing and reading preserves data types.
    """
    tf = tmpdir.join("config.cfg")

    data = {
        'int': 42,
        'float': 3.14,
        'string': 'test',
        'list': [1, 2, 3],
        'tuple': (4, 5, 6),
        'dict': {'nested': 'value'},
        'bool': True,
        'none': None,
        'numpy_array': np.array([1, 2, 3]),
    }

    configfile.writeConfigFile(data, tf)
    config = configfile.readConfigFile(tf)

    assert config['int'] == 42
    assert config['float'] == 3.14
    assert config['string'] == 'test'
    assert config['list'] == [1, 2, 3]
    assert config['tuple'] == (4, 5, 6)
    assert config['dict'] == {'nested': 'value'}
    assert config['bool'] is True
    assert config['none'] is None
    assert np.array_equal(config['numpy_array'], np.array([1, 2, 3]))
