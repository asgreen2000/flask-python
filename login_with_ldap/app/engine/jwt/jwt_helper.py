import jwt
from datetime import datetime, timedelta
from functools import wraps
# flask imports
from flask import Flask, request
from app import app
from app.constants.response import APIStatus, Response
from app.engine.jwt.models.jwt_result import JwtResult
from app.engine.user.models import User


def generate_token(user: User, is_refresh: bool = False) -> JwtResult:
    # generate a token
    try:
        payload = {
            'exp': datetime.utcnow() + timedelta(days=2 if is_refresh else 1),
            'iat': datetime.utcnow(),
            'sub': user.get_id()
        }
        token = jwt.encode(
            payload,
            app.config['SECRET_KEY'],
            algorithm='HS256'
        )
        return JwtResult(token, payload['exp'])
    except Exception as e:
        app.logger.error(e)
        raise e


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # check if Bearer token in header
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        if not token:
            return Response(APIStatus.UNAUTHORIZED).to_json()
        # split bearer token
        token = token.split(' ')[1]
        
        try:
            # decode token
            payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            # get user from payload
            
            # get userId from payload
            userId = payload['sub']
            return f(userId, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            app.logger.error('Token is invalid')
            return Response(APIStatus.EX_PIRED_TOKEN).to_json()
        except jwt.InvalidTokenError:
            app.logger.error('Token is invalid')
            return Response(APIStatus.INVALID_TOKEN).to_json()
        except Exception as e:
            app.logger.error(e)
            return Response(APIStatus.SERVER_ERROR).to_json()
        
        
  
    return decorated


