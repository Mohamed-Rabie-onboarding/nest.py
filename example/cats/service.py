from nest import injectable
from .model import CatModel
from random import random
from math import floor


def findIndex(l: list, cb):
    i = 0
    while i < len(l):
        if cb(l[i]):
            return i
        i += 1
    return -1


@injectable()
class CatsService:
    def __init__(self):
        self.__cats = []

    def get_cats(self):
        return [cat.dict() for cat in self.__cats]

    def get_cat_by_id(self, id: float):
        idx = findIndex(self.__cats, lambda c: c.id == id)

        if idx == -1:
            return None
        return self.__cats[idx].dict()

    def add_cat(self, name: str):
        cat = CatModel(floor(random() * 700), name)
        self.__cats.append(cat)
        return cat.dict()

    def update_cat(self, id: float, name: str):
        idx = findIndex(self.__cats, lambda c: c.id == id)

        if idx == -1:
            return None
        cat = self.__cats[idx]
        cat.name = name
        return cat.dict()

    def delete_cat(self, id: float):
        idx = findIndex(self.__cats, lambda c: c.id == id)

        if idx == -1:
            return None
        del self.__cats[idx]
        return True
