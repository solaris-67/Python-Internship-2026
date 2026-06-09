from os import path
from uuid import uuid4
from flask_restx import Resource
from flask_jwt_extended import jwt_required

from src.ext import api
from src.models.photo import Photo
from src.endpoints.product import product_model, product_delete_parser, product_ns, product_create_parser
from src.config import Config

@product_ns.route('/')
class ProductAPI(Resource):

    @product_ns.marshal_with(product_model)
    def get(self):
        products = Product.query.all()

        return products, 200

    @jwt_required()
    @product_ns.doc(parser=product_create_parser, security='JsonWebToken')
    def post(self):
        args = product_create_parser.parse_args()

        file = args['img']
        new_file_name = uuid4()
        filename, ext = path.splitext(file.filename)

        file.save(path.join(Config.UPLOAD_PATH, 'uploads', filename + ext))

        new_product = Product(name=args['name'], price=args['price'], img=f'uploads/{new_file_name}{ext}', category_id=args['category_id'])
        new_product.create()

        return 'new product has been created', 201

    @jwt_required()
    @product_ns.doc(parser=product_delete_parser, security='JsonWebToken')
    def delete(self):
        args = product_delete_parser.parse_args()
        product = Product.query.get(args['id'])

        if not product:
            return 'Product not found', 404

        product.delete()

        return 'success', 200

