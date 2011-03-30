# ***** BEGIN LICENSE BLOCK *****
#
# For copyright and licensing please refer to COPYING.
#
# ***** END LICENSE BLOCK *****
__author__ = 'Gavin M. Roy <gmr@myyearbook.com>'
__since__ = '2011-03-29'

from decimal import Decimal
from struct import pack


def boolean(value):
    """
    Encode a boolean

    Parameters:
    - bool value

    Returns:
    - tuple of length and encoded value
    """
    if not isinstance(value, bool):
        raise ValueError("bool type required")
    return 2, pack('>cB', 't', int(value))


def decimal(value):
    """
    Encode a decimal value

    Parameters:
    - bool value

    Returns:
    - tuple of length and encoded value
    """
    if not isinstance(value, Decimal):
        raise ValueError("decimal.Decimal type required")
    value = value.normalize()
    if value._exp < 0:
        decimals = -value._exp
        raw = int(value * (Decimal(10) ** decimals))
        return 6,  pack('>cBi', 'D', decimals, raw)
    # per spec, the "decimals" octet is unsigned (!)
    return 6, pack('>cBi', 'D', 0, int(value))


def floating_point(value):
    """
    Encode a floating point value

    Parameters:
    - float value

    Returns:
    - tuple of length and encoded value
    """
    if not isinstance(value, float):
        raise ValueError("float type required")
    output = pack('>cf', 'f',  value)
    return len(output), output


def long_int(value):
    """
    Encode a long integer

    Parameters:
    - long value

    Returns:
    - tuple of length and encoded value
    """
    if not isinstance(value, long) and not isinstance(value, int):
        raise ValueError("int or long type required")
    if value < -2147483648 or value > 2147483647:
        raise ValueError("Long integer range: -2147483648 to 2147483647")
    return 5, pack('>cl', 'I', value)


def long_uint(value):
    """
    Encode a unsigned unsigned long int

    Parameters:
    - long value

    Returns:
    - tuple of length and encoded value
    """
    if not isinstance(value, long) and not isinstance(value, int):
        raise ValueError("int or long type required")
    if value < -4294967295 or value > 4294967295:
        raise ValueError("Long integer range: -4294967295 to 4294967295")
    return 5, pack('>cL', 'i', value)


def long_long_int(value):
    """
    Encode a long-long int

    Parameters:
    - long value

    Returns:
    - tuple of length and encoded value
    """
    if not isinstance(value, long) and not isinstance(value, int):
        raise ValueError("int or long type required")
    if value < -9223372036854775808 or value > 9223372036854775807:
        raise ValueError("Unsigned long-long range: \
-9223372036854775808 to 9223372036854775807")
    return 9, pack('>cq', 'L', value)


def long_long_uint(value):
    """
    Encode a unsigned long-long int

    Parameters:
    - long value

    Returns:
    - tuple of length and encoded value
    """
    if not isinstance(value, long) and not isinstance(value, int):
        raise ValueError("int or long type required")
    if value < -18446744073709551615 or value > 18446744073709551615:
        raise ValueError("Unsigned long-long range: \
-18446744073709551615 to 18446744073709551615")
    return 9, pack('>cQ', 'l', value)


def short(value):
    """
    Encode an short integer

    Parameters:
    - int value

    Returns:
    - tuple of length and encoded value
    """
    if not isinstance(value, int):
        raise ValueError("int type required")
    if value < -32768 or value > 32767:
        raise ValueError("Short range: -32768 to 32767")
    return 3, pack('>ch', 'U', value)


def string(value):
    """
    Encode a string

    Parameters:
    - str value

    Returns:
    - tuple of length and encoded value
    """
    if not isinstance(value, str) and not isinstance(value, unicode):
        raise ValueError("str or unicode type required")
    return 5 + len(value), pack('>cI', 'S', len(value)) + value


def ushort(value):
    """
    Encode an integer

    Parameters:
    - int value

    Returns:
    - tuple of length and encoded value
    """
    if not isinstance(value, int):
        raise ValueError("int type required")
    if value < -65535 or value > 65535:
        raise ValueError("Unsigned short range: -65535 to 65535")
    return 3, pack('>cH', 'u', value)
