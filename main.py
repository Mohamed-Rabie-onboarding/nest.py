from nest import NestFactory
from example.app_module import AppModule
from example.swagger_configs import swagger_configs


def main():
    app = NestFactory.create(AppModule)
    swagger_configs.setup(app, '/api-v1/docs')
    app.listen(3000, reloader=True, debug=True)


if __name__ == "__main__":
    main()
