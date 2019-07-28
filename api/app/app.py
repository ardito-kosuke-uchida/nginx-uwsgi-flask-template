from flask import Flask
from flask_restplus import Api
from . import resources


app = Flask(__name__)
api = Api(app)
resources.setup_resources(api)
