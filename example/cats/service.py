from nest import *


@Injectable()
class CatsService:
    cats = [
        {"id": 0, "name": 'cat 0'},
        {"id": 1, "name": 'cat 1'},
        {"id": 2, "name": 'cat 2'},
    ]

    def get_cats(self):
        return self.cats
