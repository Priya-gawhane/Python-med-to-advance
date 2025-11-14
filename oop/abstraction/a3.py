from abc import ABC, abstractmethod

# Abstract Base Class
class Database(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def execute_query(self, query):
        pass


# MySQL Database Implementation
class MySQLDatabase(Database):

    def connect(self):
        print("Connecting to MySQL database...")

    def disconnect(self):
        print("Disconnecting from MySQL database...")

    def execute_query(self, query):
        print(f"Executing MySQL query: {query}")


# PostgreSQL Database Implementation
class PostgreSQLDatabase(Database):

    def connect(self):
        print("Connecting to PostgreSQL database...")

    def disconnect(self):
        print("Disconnecting from PostgreSQL database...")

    def execute_query(self, query):
        print(f"Executing PostgreSQL query: {query}")


# MongoDB Database Implementation
class MongoDBDatabase(Database):

    def connect(self):
        print("Connecting to MongoDB database...")

    def disconnect(self):
        print("Disconnecting from MongoDB database...")

    def execute_query(self, query):
        print(f"Executing MongoDB operation: {query}")


# Example usage
if __name__ == "__main__":
    dbs = [
        MySQLDatabase(),
        PostgreSQLDatabase(),
        MongoDBDatabase()
    ]

    for db in dbs:
        db.connect()
        db.execute_query("SELECT * FROM users")
        db.disconnect()
        print("-" * 40)
