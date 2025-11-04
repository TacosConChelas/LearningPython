"""
3 ) ---
Define an abstract class DatabaseConnection with:
    connect()
    disconnect()
    Subclasses: MySQLConnection, MongoDBConnection that implement both methods.
"""
from abc import ABC, abstractmethod

class DatabaseConnection(ABC):
    def __init__(self, connection : bool = False) -> None:
        super().__init__()
        self._connection = connection
    @abstractmethod
    def connect(self) -> str:
        pass
    @abstractmethod
    def disconnect(self) -> str:
        pass
    def get_status_connecction(self) -> str:
        return "On" if self._connection else "Off"
    def __repr__(self) -> str:
        return (f"<---------Info---------->\n"
        f"The {self.__class__.__name__}\n"
        f"Status: {self.get_status_connecction()}")
class MySQLConnection(DatabaseConnection):
    def __init__(self, connection: bool) -> None:
        super().__init__(connection)
    def connect(self) -> str:
        self._connection = True
        return self.__class__.__name__ + " is connected ..."
    def disconnect(self) -> str:
        self._connection = False
        return self.__class__.__name__ + " is disconnected ..."
class MongoDBConnection(DatabaseConnection):
    def __init__(self, connection: bool) -> None:
        super().__init__(connection)
    def connect(self) -> str:
        self._connection = True
        return self.__class__.__name__ + " is connected ..."
    def disconnect(self) -> str:
        self._connection = False
        return self.__class__.__name__ + " is disconnected ..."
def main() -> None:
    mysql = MySQLConnection(True)
    mongo = MongoDBConnection(False)
    print(f"\n".join(f"{db}" for db in [mysql, mongo]))

if __name__ == "__main__":
    main()
