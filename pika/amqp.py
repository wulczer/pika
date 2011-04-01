"""amqp.py

Auto-generated AMQP Support Module

WARNING: DO NOT EDIT. To Generate run tools/codegen.py

For copyright and licensing please refer to COPYING.

"""

__date__ = "2011-03-31"
__author__ = "codegen.py"

# AMQP Protocol Version
AMQP_VERSION = (0, 9, 1)

# RabbitMQ Defaults
DEFAULT_HOST = "localhost"
DEFAULT_PORT = 5672
DEFAULT_USER = "guest"
DEFAULT_PASS = "guest"

# AMQP Constants
AMQP_FRAME_METHOD = 1
AMQP_FRAME_HEADER = 2
AMQP_FRAME_BODY = 3
AMQP_FRAME_HEARTBEAT = 8
AMQP_FRAME_MIN_SIZE = 4096
AMQP_FRAME_END = 206
AMQP_REPLY_SUCCESS = 200


# AMQP Errors
class AMQPContentTooLarge(Warning):
    """Class used to map AMQP error values to an Exception
    or Warning class based upon being a hard or soft error.

    """

    name = "CONTENT-TOO-LARGE"
    value = 311


class AMQPNoRoute(Warning):
    """Class used to map AMQP error values to an Exception
    or Warning class based upon being a hard or soft error.

    """

    name = "NO-ROUTE"
    value = 312


class AMQPNoConsumers(Warning):
    """Class used to map AMQP error values to an Exception
    or Warning class based upon being a hard or soft error.

    """

    name = "NO-CONSUMERS"
    value = 313


class AMQPAccessRefused(Warning):
    """Class used to map AMQP error values to an Exception
    or Warning class based upon being a hard or soft error.

    """

    name = "ACCESS-REFUSED"
    value = 403


class AMQPNotFound(Warning):
    """Class used to map AMQP error values to an Exception
    or Warning class based upon being a hard or soft error.

    """

    name = "NOT-FOUND"
    value = 404


class AMQPResourceLocked(Warning):
    """Class used to map AMQP error values to an Exception
    or Warning class based upon being a hard or soft error.

    """

    name = "RESOURCE-LOCKED"
    value = 405


class AMQPPreconditionFailed(Warning):
    """Class used to map AMQP error values to an Exception
    or Warning class based upon being a hard or soft error.

    """

    name = "PRECONDITION-FAILED"
    value = 406


class AMQPConnectionForced(Exception):
    """Class used to map AMQP error values to an Exception
    or Warning class based upon being a hard or soft error.

    """

    name = "CONNECTION-FORCED"
    value = 320


class AMQPInvalidPath(Exception):
    """Class used to map AMQP error values to an Exception
    or Warning class based upon being a hard or soft error.

    """

    name = "INVALID-PATH"
    value = 402


class AMQPFrameError(Exception):
    """Class used to map AMQP error values to an Exception
    or Warning class based upon being a hard or soft error.

    """

    name = "FRAME-ERROR"
    value = 501


class AMQPSyntaxError(Exception):
    """Class used to map AMQP error values to an Exception
    or Warning class based upon being a hard or soft error.

    """

    name = "SYNTAX-ERROR"
    value = 502


class AMQPCommandInvalid(Exception):
    """Class used to map AMQP error values to an Exception
    or Warning class based upon being a hard or soft error.

    """

    name = "COMMAND-INVALID"
    value = 503


class AMQPChannelError(Exception):
    """Class used to map AMQP error values to an Exception
    or Warning class based upon being a hard or soft error.

    """

    name = "CHANNEL-ERROR"
    value = 504


class AMQPUnexpectedFrame(Exception):
    """Class used to map AMQP error values to an Exception
    or Warning class based upon being a hard or soft error.

    """

    name = "UNEXPECTED-FRAME"
    value = 505


class AMQPResourceError(Exception):
    """Class used to map AMQP error values to an Exception
    or Warning class based upon being a hard or soft error.

    """

    name = "RESOURCE-ERROR"
    value = 506


class AMQPNotAllowed(Exception):
    """Class used to map AMQP error values to an Exception
    or Warning class based upon being a hard or soft error.

    """

    name = "NOT-ALLOWED"
    value = 530


class AMQPNotImplemented(Exception):
    """Class used to map AMQP error values to an Exception
    or Warning class based upon being a hard or soft error.

    """

    name = "NOT-IMPLEMENTED"
    value = 540


class AMQPInternalError(Exception):
    """Class used to map AMQP error values to an Exception
    or Warning class based upon being a hard or soft error.

    """

    name = "INTERNAL-ERROR"
    value = 541


# AMQP Error code to class mapping
AMQP_ERRORS = {320: AMQPConnectionForced,
               505: AMQPUnexpectedFrame,
               502: AMQPSyntaxError,
               503: AMQPCommandInvalid,
               530: AMQPNotAllowed,
               504: AMQPChannelError,
               402: AMQPInvalidPath,
               403: AMQPAccessRefused,
               404: AMQPNotFound,
               405: AMQPResourceLocked,
               406: AMQPPreconditionFailed,
               311: AMQPContentTooLarge,
               312: AMQPNoRoute,
               313: AMQPNoConsumers,
               506: AMQPResourceError,
               540: AMQPNotImplemented,
               541: AMQPInternalError,
               501: AMQPFrameError}
