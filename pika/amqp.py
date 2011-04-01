"""amqp.py

Auto-generated AMQP Support Module

WARNING: DO NOT EDIT. To Generate run tools/codegen.py

For copyright and licensing please refer to COPYING.

"""

__date__ = "2011-04-01"
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

# AMQP Classes and Methods


class Basic(object):
    """The Basic class implements the messaging capabilities described in this
     specification.

    """
    id = 60

    class Qos(object):
        # basic.qos
        id = 10

        def __init__(self, prefetch_size=0, prefetch_count=0,
                     global_=False):
            pass

    class QosOk(object):
        # basic.qos-ok
        id = 11

        def __init__(self):
            pass

    class Consume(object):
        # basic.consume
        id = 20

        def __init__(self, queue, consumer_tag, arguments, ticket=0,
                     no_local=False, no_ack=False, exclusive=False,
                     nowait=False):
            pass

    class ConsumeOk(object):
        # basic.consume-ok
        id = 21

        def __init__(self, consumer_tag):
            pass

    class Cancel(object):
        # basic.cancel
        id = 30

        def __init__(self, consumer_tag,
                     nowait=False):
            pass

    class CancelOk(object):
        # basic.cancel-ok
        id = 31

        def __init__(self, consumer_tag):
            pass

    class Publish(object):
        # basic.publish
        id = 40

        def __init__(self, exchange, routing_key, ticket=0, mandatory=False,
                     immediate=False):
            pass

    class Return(object):
        # basic.return
        id = 50

        def __init__(self, reply_code, reply_text, exchange, routing_key):
            pass

    class Deliver(object):
        # basic.deliver
        id = 60

        def __init__(self, consumer_tag, delivery_tag, exchange, routing_key,
                     redelivered=False):
            pass

    class Get(object):
        # basic.get
        id = 70

        def __init__(self, queue, ticket=0,
                     no_ack=False):
            pass

    class GetOk(object):
        # basic.get-ok
        id = 71

        def __init__(self, delivery_tag, exchange, routing_key, message_count,
                     redelivered=False):
            pass

    class GetEmpty(object):
        # basic.get-empty
        id = 72

        def __init__(self, cluster_id):
            pass

    class Ack(object):
        # basic.ack
        id = 80

        def __init__(self, delivery_tag=0,
                     multiple=False):
            pass

    class Reject(object):
        # basic.reject
        id = 90

        def __init__(self, delivery_tag,
                     requeue=True):
            pass

    class RecoverAsync(object):
        # basic.recover-async
        id = 100

        def __init__(self,
                     requeue=False):
            pass

    class Recover(object):
        # basic.recover
        id = 110

        def __init__(self,
                     requeue=False):
            pass

    class RecoverOk(object):
        # basic.recover-ok
        id = 111

        def __init__(self):
            pass

    class Nack(object):
        # basic.nack
        id = 120

        def __init__(self, delivery_tag=0, multiple=False,
                     requeue=True):
            pass


class Channel(object):
    """AMQP is a multi-channelled protocol. Channels provide a way to
     multiplex a heavyweight TCP/IP connection into several light weight
     connections. This makes the protocol more 'firewall friendly' since port
     usage is predictable. It also means that traffic shaping and other
     network QoS features can be easily employed.

    """
    id = 20

    class Open(object):
        # channel.open
        id = 10

        def __init__(self, out_of_band):
            pass

    class OpenOk(object):
        # channel.open-ok
        id = 11

        def __init__(self, channel_id):
            pass

    class Flow(object):
        # channel.flow
        id = 20

        def __init__(self, active):
            pass

    class FlowOk(object):
        # channel.flow-ok
        id = 21

        def __init__(self, active):
            pass

    class Close(object):
        # channel.close
        id = 40

        def __init__(self, reply_code, reply_text, class_id, method_id):
            pass

    class CloseOk(object):
        # channel.close-ok
        id = 41

        def __init__(self):
            pass


class Confirm(object):
    """Using standard AMQP, the only way to guarantee that a message isn't
     lost is by using transactions -- make the channel transactional, publish
     the message, commit. In this case, transactions are unnecessarily
     heavyweight and decrease throughput by a factor of 250. To remedy this, a
     confirmation mechanism was introduced.

    """
    id = 85

    class Select(object):
        # confirm.select
        id = 10

        def __init__(self,
                     nowait=False):
            pass

    class SelectOk(object):
        # confirm.select-ok
        id = 11

        def __init__(self):
            pass


class Connection(object):
    """AMQP is a connected protocol. The connection is designed to be
     long-lasting, and can carry multiple channels.

    """
    id = 10

    class Start(object):
        # connection.start
        id = 10

        def __init__(self, server_properties, version_major=0, version_minor=9,
                     mechanisms="PLAIN", locales="en_US"):
            pass

    class StartOk(object):
        # connection.start-ok
        id = 11

        def __init__(self, client_properties, response, mechanism="PLAIN",
                     locale="en_US"):
            pass

    class Secure(object):
        # connection.secure
        id = 20

        def __init__(self, challenge):
            pass

    class SecureOk(object):
        # connection.secure-ok
        id = 21

        def __init__(self, response):
            pass

    class Tune(object):
        # connection.tune
        id = 30

        def __init__(self, channel_max=0, frame_max=0,
                     heartbeat=0):
            pass

    class TuneOk(object):
        # connection.tune-ok
        id = 31

        def __init__(self, channel_max=0, frame_max=0,
                     heartbeat=0):
            pass

    class Open(object):
        # connection.open
        id = 40

        def __init__(self, capabilities, virtual_host="/",
                     insist=False):
            pass

    class OpenOk(object):
        # connection.open-ok
        id = 41

        def __init__(self, known_hosts):
            pass

    class Close(object):
        # connection.close
        id = 50

        def __init__(self, reply_code, reply_text, class_id, method_id):
            pass

    class CloseOk(object):
        # connection.close-ok
        id = 51

        def __init__(self):
            pass


class Exchange(object):
    """The exchange class lets an application manage exchanges on the server.
     This class lets the application script its own wiring (rather than
     relying on some configuration interface).

    """
    id = 40

    class Declare(object):
        # exchange.declare
        id = 10

        def __init__(self, exchange, arguments, ticket=0, type="direct",
                     passive=False, durable=False, auto_delete=False,
                     internal=False, nowait=False):
            pass

    class DeclareOk(object):
        # exchange.declare-ok
        id = 11

        def __init__(self):
            pass

    class Delete(object):
        # exchange.delete
        id = 20

        def __init__(self, exchange, ticket=0, if_unused=False,
                     nowait=False):
            pass

    class DeleteOk(object):
        # exchange.delete-ok
        id = 21

        def __init__(self):
            pass

    class Bind(object):
        # exchange.bind
        id = 30

        def __init__(self, destination, source, routing_key, arguments,
                     ticket=0, nowait=False):
            pass

    class BindOk(object):
        # exchange.bind-ok
        id = 31

        def __init__(self):
            pass

    class Unbind(object):
        # exchange.unbind
        id = 40

        def __init__(self, destination, source, routing_key, arguments,
                     ticket=0, nowait=False):
            pass

    class UnbindOk(object):
        # exchange.unbind-ok
        id = 51

        def __init__(self):
            pass


class Queue(object):
    """The queue class lets an application manage message queues on the
     server. This is a basic step in almost all applications that consume
     messages, at least to verify that an expected message queue is actually
     present.

    """
    id = 50

    class Declare(object):
        # queue.declare
        id = 10

        def __init__(self, queue, arguments, ticket=0, passive=False,
                     durable=False, exclusive=False, auto_delete=False,
                     nowait=False):
            pass

    class DeclareOk(object):
        # queue.declare-ok
        id = 11

        def __init__(self, queue, message_count, consumer_count):
            pass

    class Bind(object):
        # queue.bind
        id = 20

        def __init__(self, queue, exchange, routing_key, arguments, ticket=0,
                     nowait=False):
            pass

    class BindOk(object):
        # queue.bind-ok
        id = 21

        def __init__(self):
            pass

    class Purge(object):
        # queue.purge
        id = 30

        def __init__(self, queue, ticket=0,
                     nowait=False):
            pass

    class PurgeOk(object):
        # queue.purge-ok
        id = 31

        def __init__(self, message_count):
            pass

    class Delete(object):
        # queue.delete
        id = 40

        def __init__(self, queue, ticket=0, if_unused=False, if_empty=False,
                     nowait=False):
            pass

    class DeleteOk(object):
        # queue.delete-ok
        id = 41

        def __init__(self, message_count):
            pass

    class Unbind(object):
        # queue.unbind
        id = 50

        def __init__(self, queue, exchange, routing_key, arguments,
                     ticket=0):
            pass

    class UnbindOk(object):
        # queue.unbind-ok
        id = 51

        def __init__(self):
            pass


class Tx(object):
    """The Transaction class (tx) gives applications access to namely server
     transactions.

    """
    id = 90

    class Select(object):
        # tx.select
        id = 10

        def __init__(self):
            pass

    class SelectOk(object):
        # tx.select-ok
        id = 11

        def __init__(self):
            pass

    class Commit(object):
        # tx.commit
        id = 20

        def __init__(self):
            pass

    class CommitOk(object):
        # tx.commit-ok
        id = 21

        def __init__(self):
            pass

    class Rollback(object):
        """This method abandons all message publications and acknowledgments
         performed in the current transaction. A new transaction starts
         immediately after a rollback. Note that unacked messages will not be
         automatically redelivered by rollback; if that is required an
         explicit recover call should be issued.

        """
        id = 30

        def __init__(self):
            pass

    class RollbackOk(object):
        """tx.rollback-ok is sent in reply to a successful tx.rollback command
         issued to RabbitMQ.

        """
        id = 31

        def __init__(self):
            pass
