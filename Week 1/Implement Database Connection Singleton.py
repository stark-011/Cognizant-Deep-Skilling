class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection_string = "sqlite:///inventory.db"
        return cls._instance

    def connect(self):
        return f"Connected to {self.connection_string}"


if __name__ == "__main__":
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()

    print(db1 is db2)
    print(db1.connect())
