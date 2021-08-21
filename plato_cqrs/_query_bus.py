import threading
from ._query_handler import QueryHandler
from ._query import Query
from ._query_response import QueryResponse
from ._exceptions import QueryAlreadyExistException
from ._exceptions import QueryHandlerDoesNotExistException
import threading


class QueryBus:
    def __init__(self):
        self._querys = {}
        self._semaphore = threading.Semaphore()

    def subscribe(self, query: Query, handler: QueryHandler):
        if query in self._querys:
            raise QueryAlreadyExistException()
        self._querys[query] = handler

    def publish(self, query: Query) -> QueryResponse:
        if query.__class__ not in self._querys:
            raise QueryHandlerDoesNotExistException()
        self._semaphore.acquire()
        response: QueryResponse = self._querys[query.__class__].handle(query)
        self._semaphore.release()
        return response

    def clean(self):
        self._querys = {}
