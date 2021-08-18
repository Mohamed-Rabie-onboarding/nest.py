class UserModel:

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name
        )
