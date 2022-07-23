import jwt
from datetime import datetime, timedelta
from functools import wraps
# flask imports
from flask import Flask, request, jsonify, make_response
from app import app
import json
from app.engine.jwt.models.jwt_result import JwtResult
from app.engine.user.models import User


def generate_token(user: User) -> JwtResult:
    # generate a token
    try:
        payload = {
            'exp': datetime.utcnow() + timedelta(days=1),
            'iat': datetime.utcnow(),
            'sub': user.toJSON()
        }
        token = jwt.encode(
            payload,
            app.config['SECRET_KEY'],
            algorithm='HS256'
        )
        return JwtResult(token, payload['exp'])
    except Exception as e:
        raise e


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        # return 401 if token is not passed
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401
  
        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, app.config['SECRET_KEY'])
            # fetch the user id from the payload
            user: User = data['sub']
            
        except:
            return jsonify({
                'message' : 'Token is invalid !!'
            }), 401
        # returns the current logged in users contex to the routes
        return f(user, *args, **kwargs)
  
    return decorated


