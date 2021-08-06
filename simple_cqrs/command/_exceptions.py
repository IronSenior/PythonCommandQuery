class CommandBusException(Exception):
    pass


class CommandAlreadyExistException(CommandBusException):
    pass


class CommandHandlerDoesNotExistException(CommandBusException):
    pass
