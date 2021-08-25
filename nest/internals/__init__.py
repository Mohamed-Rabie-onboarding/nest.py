from .module import Module


class Internals:

    @staticmethod
    def compile(AppModule):
        return Module.compile(AppModule)

    @staticmethod
    def resolve(tree):
        return Module.resolve(tree)
