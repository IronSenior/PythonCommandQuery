from ._command_handler import CommandHandler
from ._command import Command
from ._exceptions import CommandAlreadyExistException
from ._exceptions import CommandHandlerDoesNotExistException
import threading


class CommandBus:
    def __init__(self):
        self._commands = {}
        self._semaphore = threading.Semaphore()

    def subscribe(self, cmd: type, handler: CommandHandler):
        if cmd in self._commands:
            raise CommandAlreadyExistException()
        self._commands[cmd] = handler

    def publish(self, cmd: Command):
        if cmd.__class__ not in self._commands:
            raise CommandHandlerDoesNotExistException()
        self._semaphore.acquire()
        self._commands[cmd.__class__].handle(cmd)
        self._semaphore.release()
        
    def clean(self):
        self._commands = {}
