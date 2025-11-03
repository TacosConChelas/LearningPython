"""
3 ) ---
Define an abstract class DatabaseConnection with:
    connect()
    disconnect()
    Subclasses: MySQLConnection, MongoDBConnection that implement both methods.
"""
from abc import ABC, abstractmethod

class DatabaseConnection(ABC):
    def __init__(self, connection : bool) -> None:
        super().__init__()
        self._connection = connection
    @abstractmethod
    def connect(self) -> str:
        self._connection = True
        return self.__class__.__name__ + " is connected ..."
    @abstractmethod
    def disconnect(self):
        self._connection = False
        return self.__class__.__name__ + " is disconnected ..."
    def __repr__(self) -> str:
        return f"The {self.__class__.__name__}"
