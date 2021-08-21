import unittest
from unittest.mock import Mock
from .._command_bus import CommandBus
from .._command import Command
from .._command_handler import CommandHandler
from .._exceptions import CommandAlreadyExistException
from .._exceptions import CommandHandlerDoesNotExistException


class TestCommandBus(unittest.TestCase):
    
    def setUp(self) -> None:
        self.mockedCommnand: Command = Mock()
        self.mockedCommnandHandler: CommandHandler = Mock()
        return super().setUp()
    
    def test_command_bus(self):
        command_bus: CommandBus = CommandBus()
        command_bus.subscribe(self.mockedCommnand.__class__, self.mockedCommnandHandler)
        command_bus.publish(self.mockedCommnand)
        self.mockedCommnandHandler.handle.assert_called_once()
        
    def test_cannot_subscribe_to_two_handlers(self):
        command_bus: CommandBus = CommandBus()
        second_command_handler: CommandHandler = Mock()
        command_bus.subscribe(self.mockedCommnand.__class__, self.mockedCommnandHandler)
        with self.assertRaises(CommandAlreadyExistException):
            command_bus.subscribe(self.mockedCommnand.__class__, second_command_handler)
            
    def test_cannot_call_a_command_without_handler(self):
        command_bus: CommandBus = CommandBus()
        with self.assertRaises(CommandHandlerDoesNotExistException):
            command_bus.publish(self.mockedCommnand)
            
    def test_clean_command_bus(self):
        command_bus: CommandBus = CommandBus()
        command_bus.subscribe(self.mockedCommnand.__class__, self.mockedCommnandHandler)
        command_bus.clean()
        self.assertEqual(command_bus._commands, {})
        