from functools import wraps
from flask_login import current_user
from flask import abort

def role_required(role):

    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):

            # 👑 OWNER = FULL ACCESS
            if current_user.role == "owner":
                return f(*args, **kwargs)

            if current_user.role != role:
                abort(403)

            return f(*args, **kwargs)

        return wrapper

    return decorator