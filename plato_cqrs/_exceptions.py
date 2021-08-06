class CommandBusException(Exception):
    pass


class CommandAlreadyExistException(CommandBusException):
    pass


class CommandHandlerDoesNotExistException(CommandBusException):
    pass

class QueryBusException(Exception):
    pass


class QueryAlreadyExistException(QueryBusException):
    pass


class QueryHandlerDoesNotExistException(QueryBusException):
    pass
