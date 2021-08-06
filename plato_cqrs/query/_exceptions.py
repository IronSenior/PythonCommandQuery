class QueryBusException(Exception):
    pass


class QueryAlreadyExistException(QueryBusException):
    pass


class QueryHandlerDoesNotExistException(QueryBusException):
    pass
