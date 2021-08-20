from bottle import Bottle


def install_plugins(app: Bottle, plugins: list):
    for plugin in plugins:
        app.install(plugin)
