class User:
    def __init__(self, identifier, name: str, email: str, age: str):
        self.identifier = identifier
        self.name = name
        self.email = email
        self.age = age

    def __repr__(self):
        return f"{self.identifier}, {self.name}, {self.email}, {self.age}"
