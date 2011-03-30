# ***** BEGIN LICENSE BLOCK *****
#
# For copyright and licensing please refer to COPYING.
#
# ***** END LICENSE BLOCK *****
"""
AMQP Data Decoder

Functions for decoding data of various types including field tables and arrays
"""
__author__ = 'Gavin M. Roy <gmr@myyearbook.com>'
__since__ = '2011-03-30'

from decimal import Decimal
from struct import unpack_from
from time import gmtime


def boolean(value):
    """
    Decode a boolean value

    Parameters:
    - str

    Returns:
    - tuple of bytes used and a bool value
    """

    return 1, bool(unpack_from('>B', value)[0])


def decimal(value):
    """
    Decode a decimal value

    Parameters:
    - str

    Returns:
    - tuple of bytes used and a Decimal value
    """
    decimals = unpack_from('>B', value)[0]
    raw = unpack_from('>i', value, 1)[0]
    return 5, Decimal(raw) * (Decimal(10) ** -decimals)


def floating_point(value):
    """
    Decode a floating point value

    Parameters:
    - str

    Returns:
    - tuple of bytes used and a float value
    """
    return 4, unpack_from('>f', value)[0]


def long_int(value):
    """
    Decode a long integer value

    Parameters:
    - str

    Returns:
    - tuple of bytes used and an int value
    """
    return 4, unpack_from('>l', value)[0]


def long_long_int(value):
    """
    Decode a long-long integer value

    Parameters:
    - str

    Returns:
    - tuple of bytes used and an int value
    """
    return 8, unpack_from('>q', value)[0]


def short_int(value):
    """
    Decode a short integer value

    Parameters:
    - str

    Returns:
    - tuple of bytes used and an int value
    """
    return 2, unpack_from('>h', value)[0]


def string(value):
    """
    Decode a string value

    Parameters:
    - str

    Returns:
    - tuple of bytes used and an str value
    """
    length = unpack_from('>I', value)[0]
    return length + 4, value[4:length + 4]


def timestamp(value):
    """
    Decode a timestamp value

    Parameters:
    - str

    Returns:
    - tuple of bytes used and an struct_time value
    """
    return 8, gmtime(unpack_from('>Q', value)[0])


def field_array(value):
    """
    Decode a field array value

    Parameters:
    - str

    Returns:
    - tuple of bytes used and a list of values
    """
    length = unpack_from('>l', value)[0]
    offset = 4
    data = list()
    field_array_end = offset + length
    while offset < field_array_end:
        consumed, result = _decode_value(value[offset:])
        offset += consumed
        data.append(result)
    return field_array_end, data


def field_table(value):
    """
    Decode a field array value

    Parameters:
    - str

    Returns:
    - tuple of bytes used and a dict
    """
    length = unpack_from('>l', value)[0]
    offset = 4
    data = dict()
    field_table_end = offset + length
    while offset < field_table_end:
        keysize = unpack_from('B', value, offset)[0] + 1
        key = value[offset + 1:offset + keysize]
        offset += keysize
        consumed, result = _decode_value(value[offset:])
        offset += consumed
        data[key] = result
    return field_table_end, data


def _decode_value(value):
    """
    Takes in a value looking at the first byte to determine which decoder to
    use.

    Parameters:
    - str

    Returns:
    - tuple of bytes consumed and mixed value based on field type
    """
    # Determine the field type and encode it
    if value[0] == 'A':
        consumed, result = field_array(value[1:])
    elif value[0] == 'D':
        consumed, result = decimal(value[1:])
    elif value[0] == 'f':
        consumed, result = floating_point(value[1:])
    elif value[0] == 'F':
        consumed, result = field_table(value[1:])
    elif value[0] == 'I':
        consumed, result = long_int(value[1:])
    elif value[0] == 'L':
        consumed, result = long_long_int(value[1:])
    elif value[0] == 't':
        consumed, result = boolean(value[1:])
    elif value[0] == 'T':
        consumed, result = timestamp(value[1:])
    elif value[0] == 's' or value[0] == 'S':
        consumed, result = string(value[1:])
    elif value[0] == 'U':
        consumed, result = short_int(value[1:])
    else:
        raise ValueError("Unknown type: %s", value[0])
    # Return the bytes used and the decoded value
    return consumed + 1, result
