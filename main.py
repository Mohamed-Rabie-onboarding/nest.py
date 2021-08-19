from nest import NestFactory
from example.app.module import AppModule


def main():
    app = NestFactory.create(AppModule)
    app.run(port=3000, reloader=False)


if __name__ == "__main__":
    main()
