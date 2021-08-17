from example.app.module import AppModule
from nest import *


def main():
    app = NestFactory.create(AppModule)

    # const app = await NestFactory.create(AppModule);
    # await app.listen(3000);


main()
