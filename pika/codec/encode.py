# ***** BEGIN LICENSE BLOCK *****
#
# For copyright and licensing please refer to COPYING.
#
# ***** END LICENSE BLOCK *****
"""
AMQP Data Encoder

Functions for encoding data of various types including field tables and arrays
"""
__author__ = 'Gavin M. Roy <gmr@myyearbook.com>'
__since__ = '2011-03-29'

from calendar import timegm
from decimal import Decimal
from datetime import datetime
from struct import pack
from time import struct_time


def boolean(value):
    """
    Encode a boolean

    Parameters:
    - bool value

    Returns:
    - encoded value
    """
    if not isinstance(value, bool):
        raise ValueError("bool type required")
    return pack('>cB', 't', int(value))


def decimal(value):
    """
    Encode a decimal value

    Parameters:
    - bool value

    Returns:
    - encoded value
    """
    if not isinstance(value, Decimal):
        raise ValueError("decimal.Decimal type required")
    value = value.normalize()
    if value._exp < 0:
        decimals = -value._exp
        raw = int(value * (Decimal(10) ** decimals))
        return pack('>cBi', 'D', decimals, raw)
    # per spec, the "decimals" octet is unsigned (!)
    return pack('>cBi', 'D', 0, int(value))


def floating_point(value):
    """
    Encode a floating point value

    Parameters:
    - float value

    Returns:
    - encoded value
    """
    if not isinstance(value, float):
        raise ValueError("float type required")
    return pack('>cf', 'f',  value)


def long_int(value):
    """
    Encode a long integer

    Parameters:
    - long value

    Returns:
    - encoded value
    """
    if not isinstance(value, long) and not isinstance(value, int):
        raise ValueError("int or long type required")
    if value < -2147483648 or value > 2147483647:
        raise ValueError("Long integer range: -2147483648 to 2147483647")
    return pack('>cl', 'I', value)


def long_long_int(value):
    """
    Encode a long-long int

    Parameters:
    - long value

    Returns:
    - encoded value
    """
    if not isinstance(value, long) and not isinstance(value, int):
        raise ValueError("int or long type required")
    if value < -9223372036854775808 or value > 9223372036854775807:
        raise ValueError("long-long integer range: \
-9223372036854775808 to 9223372036854775807")
    return pack('>cq', 'L', value)


def short(value):
    """
    Encode an short integer

    Parameters:
    - int value

    Returns:
    - encoded value
    """
    if not isinstance(value, int):
        raise ValueError("int type required")
    if value < -32768 or value > 32767:
        raise ValueError("Short range: -32768 to 32767")
    return pack('>ch', 'U', value)


def string(value):
    """
    Encode a string

    Parameters:
    - str value

    Returns:
    - encoded value
    """
    if not isinstance(value, str) and not isinstance(value, unicode):
        raise ValueError("str or unicode type required")
    return pack('>cI', 'S', len(value)) + value


def timestamp(value):
    """
    Encode an datetime object or struct_time

    Parameters:
    - datetime or struct_time value

    Returns:
    - encoded value
    """
    if isinstance(value, datetime):
        value = value.timetuple()
    if isinstance(value, struct_time):
        return pack('>cQ', 'T', timegm(value))
    raise ValueError("datetime or struct_time type required")


def field_array(value):
    """
    Encode a field array from a dictionary

    Parameters:
    - list

    Returns:
    - encoded value
    """
    if not isinstance(value, list):
        raise ValueError("list type required")

    data = list()
    for item in value:
        data.append(_encode_value(item))

    output = ''.join(data)
    return pack('>cI', 'A', len(output)) + output


def field_table(value):
    """
    Encode a field table from a dictionary

    Parameters:
    - dict

    Returns:
    - encoded value
    """
    # If there is no value, return a standard 4 null bytes
    if not value:
        return '\x00\x00\x00\x00'

    if not isinstance(value, dict):
        raise ValueError("dict type required, got %s", type(value))

    # Iterate through all of the keys and encode the data into a table
    data = list()
    for key in value.keys():

        # Append the field header / delimiter
        data.append(pack('B', len(key)))
        data.append(key)
        try:
            data.append(_encode_value(value[key]))
        except ValueError as err:
            raise ValueError("%s error: %s", key, err)

    # Join all of the data together as a string
    output = ''.join(data)
    return pack('>I', len(output)) + output


def _encode_integer(value):
    """
    Determines the best type of numeric type to encode value as, preferring
    the smallest data size first.

    Parameters:
    - int/long

    Returns:
    - string
    """
    # Send the appropriately sized data value
    if value > -32768 and value < 32767:
        result = short(int(value))
    elif value > -2147483648 and value < 2147483647:
        result = long_int(long(value))
    elif value > -9223372036854775808 and value < 9223372036854775807:
        result = long_long_int(long(value))
    else:
        raise ValueError("Numeric value exceeds long-long-int max: %r",
                         value)
    # Return the encoded value
    return result


def _encode_value(value):
    """
    Takes a value of any type and tries to encode it with the proper encoder

    Parameters:
    - mixed

    Returns:
    - str
    """
    # Determine the field type and encode it
    if isinstance(value, bool):
        result = boolean(value)
    elif isinstance(value, int) or isinstance(value, long):
        result = _encode_integer(value)
    elif isinstance(value, Decimal):
        result = decimal(value)
    elif isinstance(value, float):
        result = floating_point(value)
    elif isinstance(value, str):
        result = string(value)
    elif isinstance(value, datetime) or isinstance(value, struct_time):
        result = timestamp(value)
    elif isinstance(value, dict):
        result = field_table(value)
    elif isinstance(value, list):
        result = field_array(value)
    else:
        raise ValueError("Unknown type: %s (%r)", type(value), value)
    # Return the encoded value
    return result
