from example.app.module import AppModule
from nest import *


def main():
    app = NestFactory.create(AppModule)
    # print(app.routes)
    app.run(port=3000)


main()
