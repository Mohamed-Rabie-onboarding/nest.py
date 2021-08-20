from typing import List
from bottle import Bottle


def merge_apps(apps: List[Bottle]):
    app = Bottle()

    for __app in apps:
        app.merge(__app)

    return app
