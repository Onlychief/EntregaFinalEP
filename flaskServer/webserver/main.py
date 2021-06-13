from apps.api import create_app_api
from flask import Flask
app = Flask(__name__, template_folder = 'template')

if __name__ == '__main__':
    create_app_api() 