from flask import Blueprint, request
from models import db, User
from flask_jwt_extended import create_access_token
import bcrypt

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")


# Register a new user
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if not data:
        return {"error": "Invalid JSON data"}, 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return {"error": "Email and password required"}, 400

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return {"error": "User already exists"}, 400

    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    hashed_password = hashed.decode("utf-8")

    new_user = User(
        email=email,
        password=hashed_password
    )

    db.session.add(new_user)
    db.session.commit()

    return {"message": "User created"}, 201


# Login user and return JWT token
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return {"error": "Invalid JSON data"}, 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return {"error": "Email and password required"}, 400

    user = User.query.filter_by(email=email).first()

    if not user:
        return {"error": "Invalid credentials"}, 401

    if not bcrypt.checkpw(
        password.encode("utf-8"),
        user.password.encode("utf-8")
    ):
        return {"error": "Invalid credentials"}, 401

    token = create_access_token(identity=str(user.id))

    return {
        "token": token,
        "user": {
            "id": user.id,
            "email": user.email
        }
    }, 200