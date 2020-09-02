from src.app import create_app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='localhost', port=8000)