class CatModel:

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
