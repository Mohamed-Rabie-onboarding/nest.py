from nest.internals import Internals
from bottle import Bottle


class NestFactory:

    def __init__(self, app: Bottle, AppModule, tree):
        self.app = app
        self.AppModule = AppModule
        self.tree = tree

    def listen(self, port: int = 3000, **kwargs):
        return self.app.run(port=port, **kwargs)

    @staticmethod
    def create(AppModule):
        tree = Internals.compile(AppModule)
        app = Internals.resolve(tree)
        return NestFactory(app, AppModule, tree)
