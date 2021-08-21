import unittest
import time
import random
from unittest.mock import Mock
from .._query_bus import QueryBus
from .._query import Query
from .._query_handler import QueryHandler
from .._query_response import QueryResponse
from .._exceptions import QueryAlreadyExistException
from .._exceptions import QueryHandlerDoesNotExistException

random.seed(time.time())


class TestQueryBus(unittest.TestCase):
    
    def setUp(self) -> None:
        self.mockedQuery: Query = Mock()
        self.mockedQueryHandler: QueryHandler = Mock()
        return super().setUp()
    
    def test_query_bus(self):
        query_bus: QueryBus = QueryBus()
        query_bus.subscribe(self.mockedQuery.__class__, self.mockedQueryHandler)
        response = query_bus.publish(self.mockedQuery)
        self.mockedQueryHandler.handle.assert_called_once()
        
    def test_query_response(self):
        query_bus: QueryBus = QueryBus()
        expected_response = random.randint(0, 900)
        query_bus.subscribe(self.mockedQuery.__class__, self.mockedQueryHandler)
        self.mockedQueryHandler.handle = Mock(return_value=expected_response)
        response = query_bus.publish(self.mockedQuery)
        self.assertEqual(expected_response, response)
        
        
    def test_cannot_subscribe_to_two_handlers(self):
        query_bus: QueryBus = QueryBus()
        second_query_handler = Mock()
        query_bus.subscribe(self.mockedQuery.__class__, self.mockedQueryHandler)
        with self.assertRaises(QueryAlreadyExistException):
            query_bus.subscribe(self.mockedQuery.__class__, second_query_handler)
            
    def test_cannot_call_a_query_without_handler(self):
        query_bus: QueryBus = QueryBus()
        with self.assertRaises(QueryHandlerDoesNotExistException):
            query_bus.publish(self.mockedQuery)

    def test_clean_query_bus(self):
        query_bus: QueryBus = QueryBus()
        query_bus.subscribe(self.mockedQuery.__class__, self.mockedQueryHandler)
        query_bus.clean()
        self.assertEqual(query_bus._querys, {})
