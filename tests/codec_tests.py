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

from datetime import datetime
from decimal import Decimal


def test_encode_bool_wrong_type():
    try:
        codec.encode.boolean('Hi')
    except ValueError:
        return
    assert False, "encode.boolean did not raise a ValueError Exception"


def test_encode_bool_false():
    check = 't\x00'
    value = codec.encode.boolean(False)
    if value != check:
        assert False, "Encoded value does not match check value: %r" % value


def test_encode_bool_true():
    check = 't\x01'
    value = codec.encode.boolean(True)
    if value != check:
        assert False, "Encoded value does not match check value: %r" % value


def test_encode_decimal_wrong_type():
    try:
        codec.encode.decimal(3.141597)
    except ValueError:
        return
    assert False, "encode.decimal did not raise a ValueError Exception"


def test_encode_decimal():
    check = 'D\x05\x00\x04\xcb/'
    value = codec.encode.decimal(Decimal('3.14159'))
    if value != check:
        assert False, "Encoded value does not match check value: %r" % value


def test_encode_decimal_whole():
    check = 'D\x00\x00\x04\xcb/'
    value = codec.encode.decimal(Decimal('314159'))
    if value != check:
        assert False, "Encoded value does not match check value: %r" % value


def test_encode_floating_point_type():
    try:
        codec.encode.floating_point("1234")
    except ValueError:
        return
    assert False, "encode.float did not raise a ValueError Exception"


def test_encode_float():
    check = 'f@I\x0f\xd0'
    value = codec.encode.floating_point(float(3.14159))
    if value != check:
        assert False, "Encoded value does not match check value: %r" % value


def test_encode_long_int_wrong_type():
    try:
        codec.encode.long_int(3.141597)
    except ValueError:
        return
    assert False, "encode.long_int did not raise a ValueError Exception"


def test_encode_long_int():
    check = 'I\x7f\xff\xff\xff'
    value = codec.encode.long_int(long(2147483647))
    if value != check:
        assert False, "Encoded value does not match check value: %r" % value


def test_encode_long_int_error():
    try:
        codec.encode.long_int(long(21474836449))
    except ValueError:
        return
    assert False, "encode.long_int did not raise a ValueError Exception"


def test_encode_long_long_int_wrong_type():
    try:
        codec.encode.long_long_int(3.141597)
    except ValueError:
        return
    assert False, "encode.long_long_int did not raise a ValueError Exception"


def test_encode_long_long_int():
    check = 'L\x7f\xff\xff\xff\xff\xff\xff\xf8'
    value = codec.encode.long_long_int(long(9223372036854775800))
    if value != check:
        assert False, "Encoded value does not match check value: %r" % value


def test_encode_long_long_int_error():
    try:
        codec.encode.long_long_int(long(9223372036854775808))
    except ValueError:
        return
    assert False, "encode.long_long_int did not raise a ValueError Exception"


def test_encode_short_wrong_type():
    try:
        codec.encode.short(3.141597)
    except ValueError:
        return
    assert False, "encode.short did not raise a ValueError Exception"


def test_encode_short():
    check = 'U\x7f\xff'
    value = codec.encode.short(32767)
    if value != check:
        assert False, "Encoded value does not match check value: %r" % value


def test_encode_short_error():
    try:
        codec.encode.short(32768)
    except ValueError:
        return
    assert False, "encode.short did not raise a ValueError Exception"


def test_encode_string():
    check = 'S\x00\x00\x00\n0123456789'
    value = codec.encode.string("0123456789")
    if value != check:
        assert False, "Encoded value does not match check value: %r" % value


def test_encode_unicode():
    check = 'S\x00\x00\x00\n0123456789'
    value = codec.encode.string(unicode("0123456789"))
    if value != check:
        assert False, "Encoded value does not match check value: %r" % value


def test_encode_string_error():
    try:
        codec.encode.string(12345.12434)
    except ValueError:
        return
    assert False, "encode.string did not raise a ValueError Exception"


def test_encode_timestamp_from_datetime():
    check = 'T\x00\x00\x00\x00Ec)\x92'
    value = datetime(2006, 11, 21, 16, 30, 10)
    value = codec.encode.timestamp(value)
    if value != check:
        assert False, "Encoded value does not match check value: %r" % value


def test_encode_timestamp_from_struct_time():
    check = 'T\x00\x00\x00\x00Ec)\x92'
    value = datetime(2006, 11, 21, 16, 30, 10).timetuple()
    value = codec.encode.timestamp(value)
    if value != check:
        assert False, "Encoded value does not match check value: %r" % value


def test_encode_timestamp_error():
    try:
        codec.encode.timestamp("hi")
    except ValueError:
        return
    assert False, "encode.timestamp did not raise a ValueError Exception"


def test_encode_field_array_error():
    try:
        codec.encode.field_array("hi")
    except ValueError:
        return
    assert False, "encode.field_array did not raise a ValueError Exception"


def test_encode_field_array():
    check = 'A\x00\x00\x00<U\x00\x01I\x00\x00\xaf\xc8S\x00\x00\x00\x04TestT\
\x00\x00\x00\x00Ec)\x92I\xbb\x9a\xca\x00D\x02\x00\x00\x01:f@H\xf5\xc3L\x00\x00\
\x00\x00\xc4e5\xffL\x80\x00\x00\x00\x00\x00\x00\x08'
    data = [1, 45000, 'Test', datetime(2006, 11, 21, 16, 30, 10),
            -1147483648, Decimal('3.14'), 3.14, long(3294967295),
            -9223372036854775800]
    value = codec.encode.field_array(data)
    if value != check:
        assert False, "Encoded value does not match check value: %r" % value


def test_encode_field_table_value_type_error():
    try:
        codec.encode.field_table({'test': object()})
    except ValueError:
        return
    assert False, "encode.field_table did not raise a ValueError Exception"


def test_encode_field_table_empty():
    value = codec.encode.field_table(None)
    if value != '\x00\x00\x00\x00':
        assert False, "Encoded value does not match check value: %r" % value


def test_encode_field_table_type_error():
    try:
        codec.encode.field_table([1, 2, 3])
    except ValueError:
        return
    assert False, "encode.field_table did not raise a ValueError Exception"


def test_encode_field_table():
    check = '\x00\x00\x00\x91\x07longvalI6e&U\x08floatvlaf@H\xf5\xc3\x07\
boolvalt\x01\x06strvalS\x00\x00\x00\x04Test\x06intvalU\x00\x01\x0ctimestampval\
T\x00\x00\x00\x00Ec)\x92\x06decvalD\x02\x00\x00\x01:\x08arrayvalA\x00\x00\x00\
\tU\x00\x01U\x00\x02U\x00\x03\x07dictval\x00\x00\x00\x0c\x03fooS\x00\x00\x00\
\x03bar'
    data = {'intval': 1,
            'strval': 'Test',
            'boolval': True,
            'timestampval': datetime(2006, 11, 21, 16, 30, 10),
            'decval': Decimal('3.14'),
            'floatvla': 3.14,
            'longval': long(912598613),
            'dictval': {'foo': 'bar'},
            'arrayval': [1, 2, 3]}
    value = codec.encode.field_table(data)
    if value != check:
        assert False, "Encoded value does not match check value: %r" % value
