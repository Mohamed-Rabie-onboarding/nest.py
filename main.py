from nest import NestFactory
from example.app_module import AppModule


def main():
    app = NestFactory.create(AppModule)
    app.listen(3000)


if __name__ == "__main__":
    main()
