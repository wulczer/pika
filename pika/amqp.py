"""amqp.py

Auto-generated AMQP Support Module

WARNING: DO NOT EDIT. To Generate run tools/codegen.py

For copyright and licensing please refer to COPYING.

"""

__date__ = "2011-05-08"
__author__ = "./codegen.py"

# AMQP Protocol Version
AMQP_VERSION = (0, 9, 1)

# RabbitMQ Defaults
DEFAULT_HOST = "localhost"
DEFAULT_PORT = 5672
DEFAULT_USER = "guest"
DEFAULT_PASS = "guest"

DEPRECATION_WARNING = "This command is deprecated in AMQP 0-9-1"
# AMQP Constants
AMQP_FRAME_METHOD = 1
AMQP_FRAME_HEADER = 2
AMQP_FRAME_BODY = 3
AMQP_FRAME_HEARTBEAT = 8
AMQP_FRAME_MIN_SIZE = 4096
AMQP_FRAME_END = 206
AMQP_REPLY_SUCCESS = 200

# AMQP data types
AMQP_DATA_TYPES = ["bit",
                   "long",
                   "longlong",
                   "longstr",
                   "octet",
                   "short",
                   "shortstr",
                   "table",
                   "timestamp"]

# AMQP domains
AMQP_DOMAINS = {"channel-id": "longstr",
                "class-id": "short",
                "consumer-tag": "shortstr",
                "delivery-tag": "longlong",
                "destination": "shortstr",
                "duration": "longlong",
                "exchange-name": "shortstr",
                "method-id": "short",
                "no-ack": "bit",
                "no-local": "bit",
                "offset": "longlong",
                "path": "shortstr",
                "peer-properties": "table",
                "queue-name": "shortstr",
                "redelivered": "bit",
                "reference": "longstr",
                "reject-code": "short",
                "reject-text": "shortstr",
                "reply-code": "short",
                "reply-text": "shortstr",
                "security-token": "longstr"}


# AMQP Errors
class AMQPContentTooLarge(Warning):
    """
    Undocumented AMQP Soft Error

    """
    name = "CONTENT-TOO-LARGE"
    value = 311


class AMQPNoRoute(Warning):
    """
    Undocumented AMQP Soft Error

    """
    name = "NO-ROUTE"
    value = 312


class AMQPNoConsumers(Warning):
    """
    Undocumented AMQP Soft Error

    """
    name = "NO-CONSUMERS"
    value = 313


class AMQPAccessRefused(Warning):
    """
    Undocumented AMQP Soft Error

    """
    name = "ACCESS-REFUSED"
    value = 403


class AMQPNotFound(Warning):
    """
    Undocumented AMQP Soft Error

    """
    name = "NOT-FOUND"
    value = 404


class AMQPResourceLocked(Warning):
    """
    Undocumented AMQP Soft Error

    """
    name = "RESOURCE-LOCKED"
    value = 405


class AMQPPreconditionFailed(Warning):
    """
    Undocumented AMQP Soft Error

    """
    name = "PRECONDITION-FAILED"
    value = 406


class AMQPConnectionForced(Exception):
    """
    Undocumented AMQP Hard Error

    """
    name = "CONNECTION-FORCED"
    value = 320


class AMQPInvalidPath(Exception):
    """
    Undocumented AMQP Hard Error

    """
    name = "INVALID-PATH"
    value = 402


class AMQPFrameError(Exception):
    """
    Undocumented AMQP Hard Error

    """
    name = "FRAME-ERROR"
    value = 501


class AMQPSyntaxError(Exception):
    """
    Undocumented AMQP Hard Error

    """
    name = "SYNTAX-ERROR"
    value = 502


class AMQPCommandInvalid(Exception):
    """
    Undocumented AMQP Hard Error

    """
    name = "COMMAND-INVALID"
    value = 503


class AMQPChannelError(Exception):
    """
    Undocumented AMQP Hard Error

    """
    name = "CHANNEL-ERROR"
    value = 504


class AMQPUnexpectedFrame(Exception):
    """
    Undocumented AMQP Hard Error

    """
    name = "UNEXPECTED-FRAME"
    value = 505


class AMQPResourceError(Exception):
    """
    Undocumented AMQP Hard Error

    """
    name = "RESOURCE-ERROR"
    value = 506


class AMQPNotAllowed(Exception):
    """
    Undocumented AMQP Hard Error

    """
    name = "NOT-ALLOWED"
    value = 530


class AMQPNotImplemented(Exception):
    """
    Undocumented AMQP Hard Error

    """
    name = "NOT-IMPLEMENTED"
    value = 540


class AMQPInternalError(Exception):
    """
    Undocumented AMQP Hard Error

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


class Connection(object):
    """Work with socket connections

    The connection class provides methods for a client to establish a network
    connection to a server, and for both peers to operate the connection
    thereafter.

    """
    # AMQP Class #
    id = 10

    class Start(object):
        """Start connection negotiation

        This method starts the connection negotiation process by telling the
        client the protocol version that the server proposes, along with a list
        of security mechanisms which the client can use for authentication.

        """
        # AMQP Method #
        id = 10

        def __init__(self, version_major=0, version_minor=9,
                     server_properties=None, mechanisms="PLAIN",
                     locales="en_US"):
            """Initialize the Connection.Start class

            :param version_major: Protocol major version.
            :type version_major: int.
            :param version_minor: Protocol minor version.
            :type version_minor: int.
            :param server_properties: Server properties.
            :type server_properties: dict.
            :param mechanisms: Available security mechanisms.
            :type mechanisms: str.
            :param locales: Available message locales.
            :type locales: str.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = True

            # Valid responses to this method
            self.valid_responses = [Connection.StartOK]

            # Protocol major version
            self.version_major = version_major

            # Protocol minor version
            self.version_minor = version_minor

            # Server properties
            self.server_properties = server_properties

            # Available security mechanisms
            self.mechanisms = mechanisms

            # Available message locales
            self.locales = locales

    class StartOK(object):
        """Select security mechanism and locale

        This method selects a SASL security mechanism.

        """
        # AMQP Method #
        id = 11

        def __init__(self, client_properties=None, mechanism="PLAIN",
                     response=None, locale="en_US"):
            """Initialize the Connection.StartOK class

            :param client_properties: Client properties.
            :type client_properties: dict.
            :param mechanism: Selected security mechanism.
            :type mechanism: str.
            :param response: Security response data.
            :type response: str.
            :param locale: Selected message locale.
            :type locale: str.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = False

            # Client properties
            self.client_properties = client_properties

            # Selected security mechanism
            self.mechanism = mechanism

            # Security response data
            self.response = response

            # Selected message locale
            self.locale = locale

    class Secure(object):
        """Security mechanism challenge

        The SASL protocol works by exchanging challenges and responses until
        both peers have received sufficient information to authenticate each
        other. This method challenges the client to provide more information.

        """
        # AMQP Method #
        id = 20

        def __init__(self, challenge=None):
            """Initialize the Connection.Secure class

            :param challenge: Security challenge data.
            :type challenge: str.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = True

            # Valid responses to this method
            self.valid_responses = [Connection.SecureOK]

            # Security challenge data
            self.challenge = challenge

    class SecureOK(object):
        """Security mechanism response

        This method attempts to authenticate, passing a block of SASL data for
        the security mechanism at the server side.

        """
        # AMQP Method #
        id = 21

        def __init__(self, response=None):
            """Initialize the Connection.SecureOK class

            :param response: Security response data.
            :type response: str.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = False

            # Security response data
            self.response = response

    class Tune(object):
        """Propose connection tuning parameters

        This method proposes a set of connection configuration values to the
        client. The client can accept and/or adjust these.

        """
        # AMQP Method #
        id = 30

        def __init__(self, channel_max=0, frame_max=0, heartbeat=0):
            """Initialize the Connection.Tune class

            :param channel_max: Proposed maximum channels.
            :type channel_max: int.
            :param frame_max: Proposed maximum frame size.
            :type frame_max: int/long.
            :param heartbeat: Desired heartbeat delay.
            :type heartbeat: int.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = True

            # Valid responses to this method
            self.valid_responses = [Connection.TuneOK]

            # Proposed maximum channels
            self.channel_max = channel_max

            # Proposed maximum frame size
            self.frame_max = frame_max

            # Desired heartbeat delay
            self.heartbeat = heartbeat

    class TuneOK(object):
        """Negotiate connection tuning parameters

        This method sends the client's connection tuning parameters to the
        server. Certain fields are negotiated, others provide capability
        information.

        """
        # AMQP Method #
        id = 31

        def __init__(self, channel_max=0, frame_max=0, heartbeat=0):
            """Initialize the Connection.TuneOK class

            :param channel_max: Negotiated maximum channels.
            :type channel_max: int.
            :param frame_max: Negotiated maximum frame size.
            :type frame_max: int/long.
            :param heartbeat: Desired heartbeat delay.
            :type heartbeat: int.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = False

            # Negotiated maximum channels
            self.channel_max = channel_max

            # Negotiated maximum frame size
            self.frame_max = frame_max

            # Desired heartbeat delay
            self.heartbeat = heartbeat

    class Open(object):
        """Open connection to virtual host

        This method opens a connection to a virtual host, which is a collection
        of resources, and acts to separate multiple application domains within
        a server. The server may apply arbitrary limits per virtual host, such
        as the number of each type of entity that may be used, per connection
        and/or in total.

        """
        # AMQP Method #
        id = 40

        def __init__(self, virtual_host="/", capabilities=None, insist=False):
            """Initialize the Connection.Open class

            :param virtual_host: Virtual host name.
            :type virtual_host: str.
            :param capabilities: Deprecated.
            :type capabilities: str.
            :param insist: Deprecated.
            :type insist: bool.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = True

            # Valid responses to this method
            self.valid_responses = [Connection.OpenOK]

            # Virtual host name
            self.virtual_host = virtual_host

            # Deprecated
            self.capabilities = capabilities

            # Deprecated
            self.insist = insist

    class OpenOK(object):
        """Signal that connection is ready

        This method signals to the client that the connection is ready for use.

        """
        # AMQP Method #
        id = 41

        def __init__(self, known_hosts=None):
            """Initialize the Connection.OpenOK class

            :param known_hosts: Deprecated.
            :type known_hosts: str.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = False

            # Deprecated
            self.known_hosts = known_hosts

    class Close(object):
        """Request a connection close

        This method indicates that the sender wants to close the connection.
        This may be due to internal conditions (e.g. a forced shut-down) or due
        to an error handling a specific method, i.e. an exception. When a close
        is due to an exception, the sender provides the class and method id of
        the method which caused the exception.

        """
        # AMQP Method #
        id = 50

        def __init__(self, reply_code=None, reply_text=None, class_id=None,
                     method_id=None):
            """Initialize the Connection.Close class

            :param reply_code: Reply code from server.
            :type reply_code: int.
            :param reply_text: Localised reply text.
            :type reply_text: str.
            :param class_id: Failing method class.
            :type class_id: int.
            :param method_id: Failing method ID.
            :type method_id: int.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = True

            # Valid responses to this method
            self.valid_responses = [Connection.CloseOK]

            # Reply code from server
            self.reply_code = reply_code

            # Localised reply text
            self.reply_text = reply_text

            # Failing method class
            self.class_id = class_id

            # Failing method ID
            self.method_id = method_id

    class CloseOK(object):
        """Confirm a connection close

        This method confirms a Connection.Close method and tells the recipient
        that it is safe to release resources for the connection and close the
        socket.

        """
        # AMQP Method #
        id = 51

        def __init__(self):
            """Initialize the Connection.CloseOK class

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = False

    class Properties(object):
        pass


class Channel(object):
    """Work with channels

    The channel class provides methods for a client to establish a channel to a
    server and for both peers to operate the channel thereafter.

    """
    # AMQP Class #
    id = 20

    class Open(object):
        """Open a channel for use

        This method opens a channel to the server.

        """
        # AMQP Method #
        id = 10

        def __init__(self, out_of_band=None):
            """Initialize the Channel.Open class

            :param out_of_band: Protocol level field, do not use, must be zero..
            :type out_of_band: str.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = True

            # Valid responses to this method
            self.valid_responses = [Channel.OpenOK]

            # Protocol level field, do not use, must be zero.
            self.out_of_band = out_of_band

    class OpenOK(object):
        """Signal that the channel is ready

        This method signals to the client that the channel is ready for use.

        """
        # AMQP Method #
        id = 11

        def __init__(self, channel_id=None):
            """Initialize the Channel.OpenOK class

            :param channel_id: Deprecated.
            :type channel_id: str.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = False

            # Deprecated
            self.channel_id = channel_id

    class Flow(object):
        """Enable/disable flow from peer

        This method asks the peer to pause or restart the flow of content data
        sent by a consumer. This is a simple flow-control mechanism that a peer
        can use to avoid overflowing its queues or otherwise finding itself
        receiving more messages than it can process. Note that this method is
        not intended for window control. It does not affect contents returned
        by Basic.Get-Ok methods.

        """
        # AMQP Method #
        id = 20

        def __init__(self, active=None):
            """Initialize the Channel.Flow class

            :param active: Start/stop content frames.
            :type active: bool.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = True

            # Valid responses to this method
            self.valid_responses = [Channel.FlowOK]

            # Start/stop content frames
            self.active = active

    class FlowOK(object):
        """Confirm a flow method

        Confirms to the peer that a flow command was received and processed.

        """
        # AMQP Method #
        id = 21

        def __init__(self, active=None):
            """Initialize the Channel.FlowOK class

            :param active: Current flow setting.
            :type active: bool.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = False

            # Current flow setting
            self.active = active

    class Close(object):
        """Request a channel close

        This method indicates that the sender wants to close the channel. This
        may be due to internal conditions (e.g. a forced shut-down) or due to
        an error handling a specific method, i.e. an exception. When a close is
        due to an exception, the sender provides the class and method id of the
        method which caused the exception.

        """
        # AMQP Method #
        id = 40

        def __init__(self, reply_code=None, reply_text=None, class_id=None,
                     method_id=None):
            """Initialize the Channel.Close class

            :param reply_code: Reply code from server.
            :type reply_code: int.
            :param reply_text: Localised reply text.
            :type reply_text: str.
            :param class_id: Failing method class.
            :type class_id: int.
            :param method_id: Failing method ID.
            :type method_id: int.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = True

            # Valid responses to this method
            self.valid_responses = [Channel.CloseOK]

            # Reply code from server
            self.reply_code = reply_code

            # Localised reply text
            self.reply_text = reply_text

            # Failing method class
            self.class_id = class_id

            # Failing method ID
            self.method_id = method_id

    class CloseOK(object):
        """Confirm a channel close

        This method confirms a Channel.Close method and tells the recipient
        that it is safe to release resources for the channel.

        """
        # AMQP Method #
        id = 41

        def __init__(self):
            """Initialize the Channel.CloseOK class

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = False


class Exchange(object):
    """Work with exchanges

    Exchanges match and distribute messages across queues. Exchanges can be
    configured in the server or declared at runtime.

    """
    # AMQP Class #
    id = 40

    class Declare(object):
        """Verify exchange exists, create if needed

        This method creates an exchange if it does not already exist, and if
        the exchange exists, verifies that it is of the correct and expected
        class.

        """
        # AMQP Method #
        id = 10

        def __init__(self, ticket=0, exchange=None, type="direct",
                     passive=False, durable=False, auto_delete=False,
                     internal=False, nowait=False, arguments="{}"):
            """Initialize the Exchange.Declare class

            :param ticket: Deprecated.
            :type ticket: int.
            :param exchange: 
            :type exchange: str.
            :param type: Exchange type.
            :type type: str.
            :param passive: Do not create exchange.
            :type passive: bool.
            :param durable: Request a durable exchange.
            :type durable: bool.
            :param auto_delete: Automatically delete when all consumers have finishing using it.
            :type auto_delete: bool.
            :param internal: Deprecated.
            :type internal: bool.
            :param nowait: Do not send a reply method.
            :type nowait: bool.
            :param arguments: Arguments for declaration.
            :type arguments: dict.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = True

            # Valid responses to this method
            self.valid_responses = [Exchange.DeclareOK]

            # Deprecated
            self.ticket = ticket

            self.exchange = exchange

            # Exchange type
            self.type = type

            # Do not create exchange
            self.passive = passive

            # Request a durable exchange
            self.durable = durable

            # Automatically delete when all consumers have finishing using it
            self.auto_delete = auto_delete

            # Deprecated
            self.internal = internal

            # Do not send a reply method
            self.nowait = nowait

            # Arguments for declaration
            self.arguments = arguments

    class DeclareOK(object):
        """Confirm exchange declaration

        This method confirms a Declare method and confirms the name of the
        exchange, essential for automatically-named exchanges.

        """
        # AMQP Method #
        id = 11

        def __init__(self):
            """Initialize the Exchange.DeclareOK class

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = False

    class Delete(object):
        """Delete an exchange

        This method deletes an exchange. When an exchange is deleted all queue
        bindings on the exchange are cancelled.

        """
        # AMQP Method #
        id = 20

        def __init__(self, ticket=0, exchange=None, if_unused=False,
                     nowait=False):
            """Initialize the Exchange.Delete class

            :param ticket: Deprecated.
            :type ticket: int.
            :param exchange: 
            :type exchange: str.
            :param if_unused: Delete only if unused.
            :type if_unused: bool.
            :param nowait: Do not send a reply method.
            :type nowait: bool.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = True

            # Valid responses to this method
            self.valid_responses = [Exchange.DeleteOK]

            # Deprecated
            self.ticket = ticket

            self.exchange = exchange

            # Delete only if unused
            self.if_unused = if_unused

            # Do not send a reply method
            self.nowait = nowait

    class DeleteOK(object):
        """Confirm deletion of an exchange

        This method confirms the deletion of an exchange.

        """
        # AMQP Method #
        id = 21

        def __init__(self):
            """Initialize the Exchange.DeleteOK class

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = False

    class Bind(object):
        """Bind exchange to an exchange

        This method binds an exchange to an exchange.

        """
        # AMQP Method #
        id = 30

        def __init__(self, ticket=0, destination=None, source=None,
                     routing_key=None, nowait=False, arguments="{}"):
            """Initialize the Exchange.Bind class

            :param ticket: Deprecated.
            :type ticket: int.
            :param destination: Name of the destination exchange to bind to.
            :type destination: str.
            :param source: Name of the source exchange to bind to.
            :type source: str.
            :param routing_key: Message routing key.
            :type routing_key: str.
            :param nowait: Do not send a reply method.
            :type nowait: bool.
            :param arguments: Arguments for binding.
            :type arguments: dict.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = True

            # Valid responses to this method
            self.valid_responses = [Exchange.BindOK]

            # Deprecated
            self.ticket = ticket

            # Name of the destination exchange to bind to
            self.destination = destination

            # Name of the source exchange to bind to
            self.source = source

            # Message routing key
            self.routing_key = routing_key

            # Do not send a reply method
            self.nowait = nowait

            # Arguments for binding
            self.arguments = arguments

    class BindOK(object):
        """Confirm bind successful

        This method confirms that the bind was successful.

        """
        # AMQP Method #
        id = 31

        def __init__(self):
            """Initialize the Exchange.BindOK class

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = False

    class Unbind(object):
        """Unbind an exchange from an exchange

        This method unbinds an exchange from an exchange.

        """
        # AMQP Method #
        id = 40

        def __init__(self, ticket=0, destination=None, source=None,
                     routing_key=None, nowait=False, arguments="{}"):
            """Initialize the Exchange.Unbind class

            :param ticket: Deprecated.
            :type ticket: int.
            :param destination: 
            :type destination: str.
            :param source: 
            :type source: str.
            :param routing_key: Routing key of binding.
            :type routing_key: str.
            :param nowait: Do not send a reply method.
            :type nowait: bool.
            :param arguments: Arguments of binding.
            :type arguments: dict.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = True

            # Valid responses to this method
            self.valid_responses = [Exchange.UnbindOK]

            # Deprecated
            self.ticket = ticket

            self.destination = destination

            self.source = source

            # Routing key of binding
            self.routing_key = routing_key

            # Do not send a reply method
            self.nowait = nowait

            # Arguments of binding
            self.arguments = arguments

    class UnbindOK(object):
        """Confirm unbind successful

        This method confirms that the unbind was successful.

        """
        # AMQP Method #
        id = 51

        def __init__(self):
            """Initialize the Exchange.UnbindOK class

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = False


class Queue(object):
    """Work with queues

    Queues store and forward messages. Queues can be configured in the server
    or created at runtime. Queues must be attached to at least one exchange in
    order to receive messages from publishers.

    """
    # AMQP Class #
    id = 50

    class Declare(object):
        """Declare queue, create if needed

        This method creates or checks a queue. When creating a new queue the
        client can specify various properties that control the durability of
        the queue and its contents, and the level of sharing for the queue.

        """
        # AMQP Method #
        id = 10

        def __init__(self, ticket=0, queue=None, passive=False, durable=False,
                     exclusive=False, auto_delete=False, nowait=False,
                     arguments="{}"):
            """Initialize the Queue.Declare class

            :param ticket: Deprecated.
            :type ticket: int.
            :param queue: 
            :type queue: str.
            :param passive: Do not create queue.
            :type passive: bool.
            :param durable: Request a durable queue.
            :type durable: bool.
            :param exclusive: Request an exclusive queue.
            :type exclusive: bool.
            :param auto_delete: Auto-delete queue when unused.
            :type auto_delete: bool.
            :param nowait: Do not send a reply method.
            :type nowait: bool.
            :param arguments: Arguments for declaration.
            :type arguments: dict.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = True

            # Valid responses to this method
            self.valid_responses = [Queue.DeclareOK]

            # Deprecated
            self.ticket = ticket

            self.queue = queue

            # Do not create queue
            self.passive = passive

            # Request a durable queue
            self.durable = durable

            # Request an exclusive queue
            self.exclusive = exclusive

            # Auto-delete queue when unused
            self.auto_delete = auto_delete

            # Do not send a reply method
            self.nowait = nowait

            # Arguments for declaration
            self.arguments = arguments

    class DeclareOK(object):
        """Confirms a queue definition

        This method confirms a Declare method and confirms the name of the
        queue, essential for automatically-named queues.

        """
        # AMQP Method #
        id = 11

        def __init__(self, queue=None, message_count=None,
                     consumer_count=None):
            """Initialize the Queue.DeclareOK class

            :param queue: 
            :type queue: str.
            :param message_count: Number of messages in queue.
            :type message_count: int/long.
            :param consumer_count: Number of consumers.
            :type consumer_count: int/long.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = False

            self.queue = queue

            # Number of messages in queue
            self.message_count = message_count

            # Number of consumers
            self.consumer_count = consumer_count

    class Bind(object):
        """Bind queue to an exchange

        This method binds a queue to an exchange. Until a queue is bound it
        will not receive any messages. In a classic messaging model, store-and-
        forward queues are bound to a direct exchange and subscription queues
        are bound to a topic exchange.

        """
        # AMQP Method #
        id = 20

        def __init__(self, ticket=0, queue=None, exchange=None,
                     routing_key=None, nowait=False, arguments="{}"):
            """Initialize the Queue.Bind class

            :param ticket: Deprecated.
            :type ticket: int.
            :param queue: 
            :type queue: str.
            :param exchange: Name of the exchange to bind to.
            :type exchange: str.
            :param routing_key: Message routing key.
            :type routing_key: str.
            :param nowait: Do not send a reply method.
            :type nowait: bool.
            :param arguments: Arguments for binding.
            :type arguments: dict.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = True

            # Valid responses to this method
            self.valid_responses = [Queue.BindOK]

            # Deprecated
            self.ticket = ticket

            self.queue = queue

            # Name of the exchange to bind to
            self.exchange = exchange

            # Message routing key
            self.routing_key = routing_key

            # Do not send a reply method
            self.nowait = nowait

            # Arguments for binding
            self.arguments = arguments

    class BindOK(object):
        """Confirm bind successful

        This method confirms that the bind was successful.

        """
        # AMQP Method #
        id = 21

        def __init__(self):
            """Initialize the Queue.BindOK class

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = False

    class Purge(object):
        """Purge a queue

        This method removes all messages from a queue which are not awaiting
        acknowledgment.

        """
        # AMQP Method #
        id = 30

        def __init__(self, ticket=0, queue=None, nowait=False):
            """Initialize the Queue.Purge class

            :param ticket: Deprecated.
            :type ticket: int.
            :param queue: 
            :type queue: str.
            :param nowait: Do not send a reply method.
            :type nowait: bool.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = True

            # Valid responses to this method
            self.valid_responses = [Queue.PurgeOK]

            # Deprecated
            self.ticket = ticket

            self.queue = queue

            # Do not send a reply method
            self.nowait = nowait

    class PurgeOK(object):
        """Confirms a queue purge

        This method confirms the purge of a queue.

        """
        # AMQP Method #
        id = 31

        def __init__(self, message_count=None):
            """Initialize the Queue.PurgeOK class

            :param message_count: 
            :type message_count: int/long.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = False

            self.message_count = message_count

    class Delete(object):
        """Delete a queue

        This method deletes a queue. When a queue is deleted any pending
        messages are sent to a dead-letter queue if this is defined in the
        server configuration, and all consumers on the queue are cancelled.

        """
        # AMQP Method #
        id = 40

        def __init__(self, ticket=0, queue=None, if_unused=False,
                     if_empty=False, nowait=False):
            """Initialize the Queue.Delete class

            :param ticket: Deprecated.
            :type ticket: int.
            :param queue: 
            :type queue: str.
            :param if_unused: Delete only if unused.
            :type if_unused: bool.
            :param if_empty: Delete only if empty.
            :type if_empty: bool.
            :param nowait: Do not send a reply method.
            :type nowait: bool.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = True

            # Valid responses to this method
            self.valid_responses = [Queue.DeleteOK]

            # Deprecated
            self.ticket = ticket

            self.queue = queue

            # Delete only if unused
            self.if_unused = if_unused

            # Delete only if empty
            self.if_empty = if_empty

            # Do not send a reply method
            self.nowait = nowait

    class DeleteOK(object):
        """Confirm deletion of a queue

        This method confirms the deletion of a queue.

        """
        # AMQP Method #
        id = 41

        def __init__(self, message_count=None):
            """Initialize the Queue.DeleteOK class

            :param message_count: 
            :type message_count: int/long.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = False

            self.message_count = message_count

    class Unbind(object):
        """Unbind a queue from an exchange

        This method unbinds a queue from an exchange.

        """
        # AMQP Method #
        id = 50

        def __init__(self, ticket=0, queue=None, exchange=None,
                     routing_key=None, arguments="{}"):
            """Initialize the Queue.Unbind class

            :param ticket: Deprecated.
            :type ticket: int.
            :param queue: 
            :type queue: str.
            :param exchange: 
            :type exchange: str.
            :param routing_key: Routing key of binding.
            :type routing_key: str.
            :param arguments: Arguments of binding.
            :type arguments: dict.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = True

            # Valid responses to this method
            self.valid_responses = [Queue.UnbindOK]

            # Deprecated
            self.ticket = ticket

            self.queue = queue

            self.exchange = exchange

            # Routing key of binding
            self.routing_key = routing_key

            # Arguments of binding
            self.arguments = arguments

    class UnbindOK(object):
        """Confirm unbind successful

        This method confirms that the unbind was successful.

        """
        # AMQP Method #
        id = 51

        def __init__(self):
            """Initialize the Queue.UnbindOK class

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = False


class Basic(object):
    """Work with basic content

    The Basic class provides methods that support an industry-standard
    messaging model.

    """
    # AMQP Class #
    id = 60

    class Qos(object):
        """Specify quality of service

        This method requests a specific quality of service. The QoS can be
        specified for the current channel or for all channels on the
        connection. The particular properties and semantics of a qos method
        always depend on the content class semantics. Though the qos method
        could in principle apply to both peers, it is currently meaningful only
        for the server.

        """
        # AMQP Method #
        id = 10

        def __init__(self, prefetch_size=0, prefetch_count=0, global_=False):
            """Initialize the Basic.Qos class

            :param prefetch_size: Prefetch window in octets.
            :type prefetch_size: int/long.
            :param prefetch_count: Prefetch window in messages.
            :type prefetch_count: int.
            :param global_: Apply to entire connection.
            :type global_: bool.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = True

            # Valid responses to this method
            self.valid_responses = [Basic.QosOK]

            # Prefetch window in octets
            self.prefetch_size = prefetch_size

            # Prefetch window in messages
            self.prefetch_count = prefetch_count

            # Apply to entire connection
            self.global_ = global_

    class QosOK(object):
        """Confirm the requested qos

        This method tells the client that the requested QoS levels could be
        handled by the server. The requested QoS applies to all active
        consumers until a new QoS is defined.

        """
        # AMQP Method #
        id = 11

        def __init__(self):
            """Initialize the Basic.QosOK class

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = False

    class Consume(object):
        """Start a queue consumer

        This method asks the server to start a "consumer", which is a transient
        request for messages from a specific queue. Consumers last as long as
        the channel they were declared on, or until the client cancels them.

        """
        # AMQP Method #
        id = 20

        def __init__(self, ticket=0, queue=None, consumer_tag=None,
                     no_local=False, no_ack=False, exclusive=False,
                     nowait=False, arguments="{}"):
            """Initialize the Basic.Consume class

            :param ticket: Deprecated.
            :type ticket: int.
            :param queue: 
            :type queue: str.
            :param consumer_tag: 
            :type consumer_tag: str.
            :param no_local: Do not deliver own messages.
            :type no_local: bool.
            :param no_ack: No acknowledgement needed.
            :type no_ack: bool.
            :param exclusive: Request exclusive access.
            :type exclusive: bool.
            :param nowait: Do not send a reply method.
            :type nowait: bool.
            :param arguments: Arguments for declaration.
            :type arguments: dict.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = True

            # Valid responses to this method
            self.valid_responses = [Basic.ConsumeOK]

            # Deprecated
            self.ticket = ticket

            self.queue = queue

            self.consumer_tag = consumer_tag

            # Do not deliver own messages
            self.no_local = no_local

            # No acknowledgement needed
            self.no_ack = no_ack

            # Request exclusive access
            self.exclusive = exclusive

            # Do not send a reply method
            self.nowait = nowait

            # Arguments for declaration
            self.arguments = arguments

    class ConsumeOK(object):
        """Confirm a new consumer

        The server provides the client with a consumer tag, which is used by
        the client for methods called on the consumer at a later stage.

        """
        # AMQP Method #
        id = 21

        def __init__(self, consumer_tag=None):
            """Initialize the Basic.ConsumeOK class

            :param consumer_tag: 
            :type consumer_tag: str.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = False

            self.consumer_tag = consumer_tag

    class Cancel(object):
        """End a queue consumer

        This method cancels a consumer. This does not affect already delivered
        messages, but it does mean the server will not send any more messages
        for that consumer. The client may receive an arbitrary number of
        messages in between sending the cancel method and receiving the cancel-
        ok reply.

        """
        # AMQP Method #
        id = 30

        def __init__(self, consumer_tag=None, nowait=False):
            """Initialize the Basic.Cancel class

            :param consumer_tag: Consumer tag.
            :type consumer_tag: str.
            :param nowait: Do not send a reply method.
            :type nowait: bool.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = True

            # Valid responses to this method
            self.valid_responses = [Basic.CancelOK]

            # Consumer tag
            self.consumer_tag = consumer_tag

            # Do not send a reply method
            self.nowait = nowait

    class CancelOK(object):
        """Confirm a cancelled consumer

        This method confirms that the cancellation was completed.

        """
        # AMQP Method #
        id = 31

        def __init__(self, consumer_tag=None):
            """Initialize the Basic.CancelOK class

            :param consumer_tag: Consumer tag.
            :type consumer_tag: str.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = False

            # Consumer tag
            self.consumer_tag = consumer_tag

    class Publish(object):
        """Publish a message

        This method publishes a message to a specific exchange. The message
        will be routed to queues as defined by the exchange configuration and
        distributed to any active consumers when the transaction, if any, is
        committed.

        """
        # AMQP Method #
        id = 40

        def __init__(self, ticket=0, exchange=None, routing_key=None,
                     mandatory=False, immediate=False):
            """Initialize the Basic.Publish class

            :param ticket: Deprecated.
            :type ticket: int.
            :param exchange: 
            :type exchange: str.
            :param routing_key: Message routing key.
            :type routing_key: str.
            :param mandatory: Indicate mandatory routing.
            :type mandatory: bool.
            :param immediate: Request immediate delivery.
            :type immediate: bool.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = False

            # Deprecated
            self.ticket = ticket

            self.exchange = exchange

            # Message routing key
            self.routing_key = routing_key

            # Indicate mandatory routing
            self.mandatory = mandatory

            # Request immediate delivery
            self.immediate = immediate

    class Return(object):
        """Return a failed message

        This method returns an undeliverable message that was published with
        the "immediate" flag set, or an unroutable message published with the
        "mandatory" flag set. The reply code and text provide information about
        the reason that the message was undeliverable.

        """
        # AMQP Method #
        id = 50

        def __init__(self, reply_code=None, reply_text=None, exchange=None,
                     routing_key=None):
            """Initialize the Basic.Return class

            :param reply_code: Reply code from server.
            :type reply_code: int.
            :param reply_text: Localised reply text.
            :type reply_text: str.
            :param exchange: 
            :type exchange: str.
            :param routing_key: Message routing key.
            :type routing_key: str.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = False

            # Reply code from server
            self.reply_code = reply_code

            # Localised reply text
            self.reply_text = reply_text

            self.exchange = exchange

            # Message routing key
            self.routing_key = routing_key

    class Deliver(object):
        """Notify the client of a consumer message

        This method delivers a message to the client, via a consumer. In the
        asynchronous message delivery model, the client starts a consumer using
        the Consume method, then the server responds with Deliver methods as
        and when messages arrive for that consumer.

        """
        # AMQP Method #
        id = 60

        def __init__(self, consumer_tag=None, delivery_tag=None,
                     redelivered=False, exchange=None, routing_key=None):
            """Initialize the Basic.Deliver class

            :param consumer_tag: Consumer tag.
            :type consumer_tag: str.
            :param delivery_tag: Server-assigned delivery tag.
            :type delivery_tag: int/long.
            :param redelivered: Message is being redelivered.
            :type redelivered: bool.
            :param exchange: 
            :type exchange: str.
            :param routing_key: Message routing key.
            :type routing_key: str.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = False

            # Consumer tag
            self.consumer_tag = consumer_tag

            # Server-assigned delivery tag
            self.delivery_tag = delivery_tag

            # Message is being redelivered
            self.redelivered = redelivered

            self.exchange = exchange

            # Message routing key
            self.routing_key = routing_key

    class Get(object):
        """Direct access to a queue

        This method provides a direct access to the messages in a queue using a
        synchronous dialogue that is designed for specific types of application
        where synchronous functionality is more important than performance.

        """
        # AMQP Method #
        id = 70

        def __init__(self, ticket=0, queue=None, no_ack=False):
            """Initialize the Basic.Get class

            :param ticket: Deprecated.
            :type ticket: int.
            :param queue: 
            :type queue: str.
            :param no_ack: No acknowledgement needed.
            :type no_ack: bool.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = True

            # Valid responses to this method
            self.valid_responses = [Basic.GetOK, Basic.GetEmpty]

            # Deprecated
            self.ticket = ticket

            self.queue = queue

            # No acknowledgement needed
            self.no_ack = no_ack

    class GetOK(object):
        """Provide client with a message

        This method delivers a message to the client following a get method. A
        message delivered by 'get-ok' must be acknowledged unless the no-ack
        option was set in the get method.

        """
        # AMQP Method #
        id = 71

        def __init__(self, delivery_tag=None, redelivered=False, exchange=None,
                     routing_key=None, message_count=None):
            """Initialize the Basic.GetOK class

            :param delivery_tag: Server-assigned delivery tag.
            :type delivery_tag: int/long.
            :param redelivered: Message is being redelivered.
            :type redelivered: bool.
            :param exchange: 
            :type exchange: str.
            :param routing_key: Message routing key.
            :type routing_key: str.
            :param message_count: Number of messages in queue.
            :type message_count: int/long.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = False

            # Server-assigned delivery tag
            self.delivery_tag = delivery_tag

            # Message is being redelivered
            self.redelivered = redelivered

            self.exchange = exchange

            # Message routing key
            self.routing_key = routing_key

            # Number of messages in queue
            self.message_count = message_count

    class GetEmpty(object):
        """Indicate no messages available

        This method tells the client that the queue has no messages available
        for the client.

        """
        # AMQP Method #
        id = 72

        def __init__(self, cluster_id=None):
            """Initialize the Basic.GetEmpty class

            :param cluster_id: Deprecated.
            :type cluster_id: str.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = False

            # Deprecated
            self.cluster_id = cluster_id

    class Ack(object):
        """Acknowledge one or more messages

        When sent by the client, this method acknowledges one or more messages
        delivered via the Deliver or Get-Ok methods.  When sent by server, this
        method acknowledges one or more messages published with the Publish
        method on a channel in confirm mode.  The acknowledgement can be for a
        single message or a set of messages up to and including a specific
        message.

        """
        # AMQP Method #
        id = 80

        def __init__(self, delivery_tag=0, multiple=False):
            """Initialize the Basic.Ack class

            :param delivery_tag: Server-assigned delivery tag.
            :type delivery_tag: int/long.
            :param multiple: Acknowledge multiple messages.
            :type multiple: bool.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = False

            # Server-assigned delivery tag
            self.delivery_tag = delivery_tag

            # Acknowledge multiple messages
            self.multiple = multiple

    class Reject(object):
        """Reject an incoming message

        This method allows a client to reject a message. It can be used to
        interrupt and cancel large incoming messages, or return untreatable
        messages to their original queue.

        """
        # AMQP Method #
        id = 90

        def __init__(self, delivery_tag=None, requeue=True):
            """Initialize the Basic.Reject class

            :param delivery_tag: Server-assigned delivery tag.
            :type delivery_tag: int/long.
            :param requeue: Requeue the message.
            :type requeue: bool.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = False

            # Server-assigned delivery tag
            self.delivery_tag = delivery_tag

            # Requeue the message
            self.requeue = requeue

    class RecoverAsync(object):
        """Redeliver unacknowledged messages

        This method asks the server to redeliver all unacknowledged messages on
        a specified channel. Zero or more messages may be redelivered.  This
        method is deprecated in favour of the synchronous Recover/Recover-Ok.

        """
        # AMQP Method #
        id = 100

        def __init__(self, requeue=False):
            """Initialize the Basic.RecoverAsync class

            :param requeue: Requeue the message.
            :type requeue: bool.

            :raises: DeprecationWarning

            """

            # This command is deprecated in AMQP 0-9-1
            raise DeprecationWarning(DEPRECATION_WARNING)

            # Specifies if this is a synchronous AMQP method
            self.synchronous = False

            # Requeue the message
            self.requeue = requeue

    class Recover(object):
        """Redeliver unacknowledged messages

        This method asks the server to redeliver all unacknowledged messages on
        a specified channel. Zero or more messages may be redelivered.  This
        method replaces the asynchronous Recover.

        """
        # AMQP Method #
        id = 110

        def __init__(self, requeue=False):
            """Initialize the Basic.Recover class

            :param requeue: Requeue the message.
            :type requeue: bool.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = True

            # Requeue the message
            self.requeue = requeue

    class RecoverOK(object):
        """Confirm recovery

        This method acknowledges a Basic.Recover method.

        """
        # AMQP Method #
        id = 111

        def __init__(self):
            """Initialize the Basic.RecoverOK class

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = False

    class Nack(object):
        """Reject one or more incoming messages

        This method allows a client to reject one or more incoming messages. It
        can be used to interrupt and cancel large incoming messages, or return
        untreatable messages to their original queue.  This method is also used
        by the server to inform publishers on channels in confirm mode of
        unhandled messages.  If a publisher receives this method, it probably
        needs to republish the offending messages.

        """
        # AMQP Method #
        id = 120

        def __init__(self, delivery_tag=0, multiple=False, requeue=True):
            """Initialize the Basic.Nack class

            :param delivery_tag: Server-assigned delivery tag.
            :type delivery_tag: int/long.
            :param multiple: Reject multiple messages.
            :type multiple: bool.
            :param requeue: Requeue the message.
            :type requeue: bool.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = False

            # Server-assigned delivery tag
            self.delivery_tag = delivery_tag

            # Reject multiple messages
            self.multiple = multiple

            # Requeue the message
            self.requeue = requeue

    class Properties(object):
        pass


class TX(object):
    """Work with transactions

    The Tx class allows publish and ack operations to be batched into atomic
    units of work.  The intention is that all publish and ack requests issued
    within a transaction will complete successfully or none of them will.
    Servers SHOULD implement atomic transactions at least where all publish or
    ack requests affect a single queue.  Transactions that cover multiple
    queues may be non-atomic, given that queues can be created and destroyed
    asynchronously, and such events do not form part of any transaction.
    Further, the behaviour of transactions with respect to the immediate and
    mandatory flags on Basic.Publish methods is not defined.

    """
    # AMQP Class #
    id = 90

    class Select(object):
        """Select standard transaction mode

        This method sets the channel to use standard transactions. The client
        must use this method at least once on a channel before using the Commit
        or Rollback methods.

        """
        # AMQP Method #
        id = 10

        def __init__(self):
            """Initialize the TX.Select class

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = True

            # Valid responses to this method
            self.valid_responses = [TX.SelectOK]

    class SelectOK(object):
        """Confirm transaction mode

        This method confirms to the client that the channel was successfully
        set to use standard transactions.

        """
        # AMQP Method #
        id = 11

        def __init__(self):
            """Initialize the TX.SelectOK class

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = False

    class Commit(object):
        """Commit the current transaction

        This method commits all message publications and acknowledgments
        performed in the current transaction.  A new transaction starts
        immediately after a commit.

        """
        # AMQP Method #
        id = 20

        def __init__(self):
            """Initialize the TX.Commit class

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = True

            # Valid responses to this method
            self.valid_responses = [TX.CommitOK]

    class CommitOK(object):
        """Confirm a successful commit

        This method confirms to the client that the commit succeeded. Note that
        if a commit fails, the server raises a channel exception.

        """
        # AMQP Method #
        id = 21

        def __init__(self):
            """Initialize the TX.CommitOK class

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = False

    class Rollback(object):
        """Abandon the current transaction

        This method abandons all message publications and acknowledgments
        performed in the current transaction. A new transaction starts
        immediately after a rollback. Note that unacked messages will not be
        automatically redelivered by rollback; if that is required an explicit
        recover call should be issued.

        """
        # AMQP Method #
        id = 30

        def __init__(self):
            """Initialize the TX.Rollback class

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = True

            # Valid responses to this method
            self.valid_responses = [TX.RollbackOK]

    class RollbackOK(object):
        """Confirm successful rollback

        This method confirms to the client that the rollback succeeded. Note
        that if an rollback fails, the server raises a channel exception.

        """
        # AMQP Method #
        id = 31

        def __init__(self):
            """Initialize the TX.RollbackOK class

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = False


class Confirm(object):
    """Work with confirms

    The Confirm class allows publishers to put the channel in confirm mode and
    susequently be notified when messages have been handled by the broker.  The
    intention is that all messages published on a channel in confirm mode will
    be acknowledged at some point.  By acknowledging a message the broker
    assumes responsibility for it and indicates that it has done something it
    deems reasonable with it.  Unroutable mandatory or immediate messages are
    acknowledged right after the Basic.Return method. Messages are acknowledged
    when all queues to which the message has been routed have either delivered
    the message and received an acknowledgement (if required), or enqueued the
    message (and persisted it if required).  Published messages are assigned
    ascending sequence numbers, starting at 1 with the first Confirm.Select
    method. The server confirms messages by sending Basic.Ack methods referring
    to these sequence numbers.

    """
    # AMQP Class #
    id = 85

    class Select(object):
        """Select confirm mode (i.e. enable publisher acknowledgements)

        This method sets the channel to use publisher acknowledgements. The
        client can only use this method on a non-transactional channel.

        """
        # AMQP Method #
        id = 10

        def __init__(self, nowait=False):
            """Initialize the Confirm.Select class

            :param nowait: Do not send a reply method.
            :type nowait: bool.

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = True

            # Valid responses to this method
            self.valid_responses = [Confirm.SelectOK]

            # Do not send a reply method
            self.nowait = nowait

    class SelectOK(object):
        """Acknowledge confirm mode

        This method confirms to the client that the channel was successfully
        set to use publisher acknowledgements.

        """
        # AMQP Method #
        id = 11

        def __init__(self):
            """Initialize the Confirm.SelectOK class

            """

            # Specifies if this is a synchronous AMQP method
            self.synchronous = False
