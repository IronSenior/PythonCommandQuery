from abc import ABC, abstractmethod
from ._query import Query


class QueryHandler(ABC):
    
    @abstractmethod
    def handle(self, query: Query):
        raise NotImplementedError()
