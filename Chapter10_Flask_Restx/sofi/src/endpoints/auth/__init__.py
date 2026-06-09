from flask_restx.reqparse import RequestParser

from src.ext import api

auth_ns = api.namespace('auth', description='Authentication API')

login_parser = RequestParser()
login_parser.add_argument('name',type=str, required=True)
login_parser.add_argument('password',type=str, required=True)
