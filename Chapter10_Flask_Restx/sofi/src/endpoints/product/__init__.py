from flask_restx import fields
from flask_restx.reqparse import RequestParser
from werkzeug.datastructures import FileStorage

from src.ext import api

product_ns = api.namespace('product', description='Product related operations')

product_delete_parser = RequestParser()
product_delete_parser.add_argument('id', type=int, required=True)

product_create_parser = RequestParser()
product_create_parser.add_argument('name', type=str, required=True, location='form')
product_create_parser.add_argument('price', type=int, required=True, location='form')
product_create_parser.add_argument('img', type=FileStorage, required=True, location='files')
product_create_parser.add_argument('category_id', type=str, required=True, location='form')


product_model = api.model('product', {'id': fields.Integer,
                                      'name': fields.String,
                                      'price': fields.Float,
                                      'category': fields.String,
                                      'img': fields.String,})

