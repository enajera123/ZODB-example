import ZODB, ZODB.FileStorage
class Connection:
    def __init__(self, fileStorageName: str):
        self.fileStorageName = fileStorageName
        self.connection = None
        self.root = None
        self.db = None
        self.connect()

    def connect(self):
        storage = ZODB.FileStorage.FileStorage(self.fileStorageName)
        self.db = ZODB.DB(storage)
        self.connection = self.db.open()
        self.root = self.connection.root()

    def close(self):
        self.connection.close()
        self.db.close()
        print("Connection closed successfully!")
