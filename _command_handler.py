from abc import ABC, abstractmethod
from ._command import Command


class CommandHandler(ABC):
    
    @abstractmethod
    def handle(self, cmd: Command):
        raise NotImplementedError()