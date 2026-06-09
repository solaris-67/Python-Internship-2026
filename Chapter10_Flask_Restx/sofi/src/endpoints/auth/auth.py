from flask_restx import Resource
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash

from src.endpoints.auth import auth_ns, login_parser
from src.models.user import User

@auth_ns.route('/login')
class LoginAPI(Resource):

    @auth_ns.doc(parser=login_parser)
    def post(self):
        args = login_parser.parse_args()

        user = User.query.filter_by(name=args['name']).first()

        if not user:
            return 'Not Found', 404

        if not check_password_hash(user.password, args['password']):
            return 'Incorrect password', 401

        response = {
            'access_token': create_access_token(identity=str(user.id), additional_claims={'role': user.role}),
            'refresh_token': create_refresh_token(identity=str(user.id))
        }

        return response, 200

@auth_ns.route('/refresh')
class RefreshAPI(Resource):
    @jwt_required(refresh=True)
    @auth_ns.doc(security='JsonWebToken')
    def post(self):
        user_id = get_jwt_identity()

        response = {'access_token': create_access_token(identity=str(user_id)), }

        return response, 200



