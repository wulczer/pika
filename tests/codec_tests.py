# ***** BEGIN LICENSE BLOCK *****
#
# For copyright and licensing please refer to COPYING.
#
# ***** END LICENSE BLOCK *****

__author__ = 'Gavin M. Roy'
__email__ = 'gmr@myyearbook.com'
__date__ = '2011-03-29'

import test_support
import pika.codec as codec

from decimal import Decimal


def test_encode_bool_wrong_type():
    try:
        codec.encode.boolean('Hi')
    except ValueError:
        return
    assert False, "encode.boolean did not raise a ValueError Exception"


def test_encode_bool_false():
    check = 't\x00'
    length, value = codec.encode.boolean(False)
    if len(value) != length:
        assert False, "Encoded value length doesn't match return length"
    if value != check:
        assert False, "Encoded value does not match check value"


def test_encode_bool_true():
    check = 't\x01'
    length, value = codec.encode.boolean(True)
    if len(value) != length:
        assert False, "Encoded value length doesn't match return length"
    if value != check:
        assert False, "Encoded value does not match check value"


def test_encode_decimal_wrong_type():
    try:
        codec.encode.decimal(3.141597)
    except ValueError:
        return
    assert False, "encode.decimal did not raise a ValueError Exception"


def test_encode_decimal():
    check = 'D\x05\x00\x04\xcb/'
    length, value = codec.encode.decimal(Decimal('3.14159'))
    if len(value) != length:
        assert False, "Encoded value length doesn't match return length"
    if value != check:
        assert False, "Encoded value does not match check value"


def test_encode_floating_point_type():
    try:
        codec.encode.floating_point("1234")
    except ValueError:
        return
    assert False, "encode.float did not raise a ValueError Exception"


def test_encode_float():
    check = 'f@I\x0f\xd0'
    length, value = codec.encode.floating_point(float(3.14159))
    if len(value) != length:
        assert False, "Encoded value length doesn't match return length"
    if value != check:
        assert False, "Encoded value does not match check value"


def test_encode_long_int_wrong_type():
    try:
        codec.encode.long_int(3.141597)
    except ValueError:
        return
    assert False, "encode.long_int did not raise a ValueError Exception"


def test_encode_long_int():
    check = 'I\x7f\xff\xff\xff'
    length, value = codec.encode.long_int(long(2147483647))
    if len(value) != length:
        assert False, "Encoded value length doesn't match return length"
    if value != check:
        assert False, "Encoded value does not match check value"


def test_encode_long_int_error():
    try:
        codec.encode.long_int(long(21474836449))
    except ValueError:
        return
    assert False, "encode.long_int did not raise a ValueError Exception"


def test_encode_long_uint_wrong_type():
    try:
        codec.encode.long_uint(3.141597)
    except ValueError:
        return
    assert False, "encode.long_int did not raise a ValueError Exception"


def test_encode_long_uint():
    check = 'i\xff\xff\xff\xff'
    length, value = codec.encode.long_uint(long(4294967295))
    if len(value) != length:
        assert False, "Encoded value length doesn't match return length"
    if value != check:
        assert False, "Encoded value does not match check value"


def test_encode_long_uint_error():
    try:
        codec.encode.long_uint(long(4294967296))
    except ValueError:
        return
    assert False, "encode.long_uint did not raise a ValueError Exception"


def test_encode_long_long_int_wrong_type():
    try:
        codec.encode.long_long_int(3.141597)
    except ValueError:
        return
    assert False, "encode.long_long_int did not raise a ValueError Exception"


def test_encode_long_long_int():
    check = 'L\x7f\xff\xff\xff\xff\xff\xff\xf8'
    length, value = codec.encode.long_long_int(long(9223372036854775800))
    if len(value) != length:
        assert False, "Encoded value length doesn't match return length"
    if value != check:
        assert False, "Encoded value does not match check value"


def test_encode_long_long_int_error():
    try:
        codec.encode.long_long_int(long(9223372036854775808))
    except ValueError:
        return
    assert False, "encode.long_long_int did not raise a ValueError Exception"


def test_encode_long_long_uint_wrong_type():
    try:
        codec.encode.long_long_uint(3.141597)
    except ValueError:
        return
    assert False, "encode.long_long_uint did not raise a ValueError Exception"


def test_encode_long_long_uint():
    check = 'l\xff\xff\xff\xff\xff\xff\xff\xff'
    length, value = codec.encode.long_long_uint(long(18446744073709551615))
    if len(value) != length:
        assert False, "Encoded value length doesn't match return length"
    if value != check:
        assert False, "Encoded value does not match check value"


def test_encode_long_long_uint_error():
    try:
        codec.encode.long_long_uint(long(18446744073709551616))
    except ValueError:
        return
    assert False, "encode.long_long_uint did not raise a ValueError Exception"


def test_encode_short_wrong_type():
    try:
        codec.encode.short(3.141597)
    except ValueError:
        return
    assert False, "encode.short did not raise a ValueError Exception"


def test_encode_short():
    check = 'U\x7f\xff'
    length, value = codec.encode.short(32767)
    if len(value) != length:
        assert False, "Encoded value length doesn't match return length"
    if value != check:
        assert False, "Encoded value does not match check value"


def test_encode_short_error():
    try:
        codec.encode.short(32768)
    except ValueError:
        return
    assert False, "encode.short did not raise a ValueError Exception"


def test_encode_ushort_wrong_type():
    try:
        codec.encode.ushort(3.141597)
    except ValueError:
        return
    assert False, "encode.ushort did not raise a ValueError Exception"


def test_encode_ushort():
    check = 'u\xff\xff'
    length, value = codec.encode.ushort(65535)
    if len(value) != length:
        assert False, "Encoded value length doesn't match return length"
    if value != check:
        assert False, "Encoded value does not match check value"


def test_encode_ushort_error():
    try:
        codec.encode.ushort(-65540)
    except ValueError:
        return
    assert False, "encode.ushort did not raise a ValueError Exception"


def test_encode_string():
    check = 'S\x00\x00\x00\n0123456789'
    length, value = codec.encode.string("0123456789")
    if len(value) != length:
        assert False, "Encoded value length doesn't match return length"
    if value != check:
        assert False, "Encoded value does not match check value"
