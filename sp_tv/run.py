#https://codeburst.io/jwt-authorization-in-flask-c63c1acf4eeb

from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from utils import request_printer

app = Flask(__name__)
# app.wsgi_app = request_printer.LoggingMiddleware(app.wsgi_app)
api = Api(app)

app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(app)

from sp_tv import views, models, resources

api.add_resource(resources.ProtectedResource, '/protected_tv')

