# ***** BEGIN LICENSE BLOCK *****
#
# For copyright and licensing please refer to COPYING.
#
# ***** END LICENSE BLOCK *****

__author__ = 'Gavin M. Roy'
__email__ = 'gmr@myyearbook.com'
__date__ = '2011-04-10'

import amqp
from codec import decode, encode
from struct import pack, unpack, unpack_from, error as struct_error

CONTENT_FRAME_HEADER_SIZE = 7
CONTENT_FRAME_END_SIZE = 1
CONTENT_FRAME_END_BYTE = 206


def decode_frame(data_in):
    """Takes in binary data and maps builds the appropriate frame type,
    returning a frame object.

    Arguments:

    - unicode binary frame data

    Returns

    - tuple
        - Bytes used
        - object or None
    """
    # Look to see if it's a protocol header frame
    try:
        if data_in[0:4] == 'AMQP':
            major, minor, revision = unpack_from('BBB', data_in, 5)
            return 8, ProtocolHeader(major, minor, revision)
    except IndexError:
        # We didn't get a full frame
        return 0, None
    except struct_error:
        # We didn't get a full frame
        return 0, None

    # Get the Frame Type, Channel Number and Frame Size
    try:
        frame_type, channel_number, frame_size = \
            unpack('>BHL', data_in[0:CONTENT_FRAME_HEADER_SIZE])
    except struct_error:
        # We didn't get a full frame
        return 0, None

    # Get the frame data size
    frame_end = data_in.find(chr(amqp.AMQP_FRAME_END))

    # We don't have all of the frame yet
    if frame_end > len(data_in):
        return 0, None

    # The Frame termination chr is wrong
    if data_in[frame_end] != chr(CONTENT_FRAME_END_BYTE):
        raise amqp.AMQPFrameError("Invalid CONTENT_FRAME_END_BYTE marker")

    # Get the raw frame data
    frame_data = data_in[CONTENT_FRAME_HEADER_SIZE:frame_end]

    # If it's a method frame,
    if frame_type == amqp.AMQP_FRAME_METHOD:

        # Get the Method Index from the class data
        bytes_used, method_index = decode.long_int(frame_data)
        offset = bytes_used

        # Create a method frame object
        method = MethodFrame(channel_number,
                             method_index,
                             frame_data[offset:])

        # Return the amount of data consumed and the Method object
        return frame_end + 1, method

    """
    elif frame_type == spec.FRAME_HEADER:

        # Return the header class and body size
        class_id, weight, body_size = unpack_from('>HHQ', frame_data)

        # Get the Properties type
        properties = spec.props[class_id]()

        log.debug("<%r>", properties)

        # Decode the properties
        out = properties.decode(frame_data[12:])

        log.debug("<%r>", out)

        # Return a Header frame
        return frame_end, Header(channel_number, body_size, properties)

    elif frame_type == spec.FRAME_BODY:

        # Return the amount of data consumed and the Body frame w/ data
        return frame_end, Body(channel_number, frame_data)

    elif frame_type == spec.FRAME_HEARTBEAT:

        # Return the amount of data and a Heartbeat frame
        return frame_end, Heartbeat()

    raise exceptions.InvalidFrameError("Unknown frame type: %i" % frame_type)
    """





class ProtocolHeader(object):

    def __init__(self, major_version=None, minor_version=None, revision=None):
        """
        Construct a Protocol Header frame object for the specified AMQP version

        Parameters:

        - major: int
        - miinor: int
        - revision: int
        """
        self.major_version = major_version or amqp.AMQP_VERSION[0]
        self.minor_version = minor_version or amqp.AMQP_VERSION[1]
        self.revision = revision or amqp.AMQP_VERSION[2]

    def marshal(self):
        """
        Return the full AMQP wire protocol frame data representation of the
        ProtocolHeader frame
        """
        return 'AMQP' + pack('BBBB', 0,
                             self.major_version,
                             self.minor_version,
                             self.revision)


class MethodFrame(object):

    def __init__(self, channel, method_index, data_in=None):
        """Represents an AMQP Method Frame

        Parameters:

        - int: Channel number
        - int: AMQP Frame Class
        - int: AMQP Frame Method
        - bytes: frame data

        """
        self.channel = channel
        self.method_class = amqp.INDEX_MAPPING[method_index]
        self.frame = self.method_class()

        # If we were passed data, decode it
        if data_in:
            self._decode(data_in)

    def marshall(self):
        pass
        #return struct.pack('>BHI',
        #                   self.frame_type,
        #                   self.channel_number,
        #                   len(payload)) + payload + chr(spec.FRAME_END)

    def _decode(self, data):
        """Decodes data applying the data in order as specified in the amqp
        class/method definition

        Parameters:

        - bytes: data to decode
        """
        for key in self.method_class.arguments:
            consumed, value = \
                decode.decode_by_type(data, getattr(self.method_class, key))
            data = data[consumed:]
            setattr(self.frame, key, value)
