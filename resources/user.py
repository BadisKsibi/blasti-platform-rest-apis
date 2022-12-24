from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
import requests
import os
from flask_jwt_extended import (create_access_token,get_jwt,jwt_required)

from db import db
from models import UserModel
from schemas import UserSchema
from blocklist import BLOCKLIST

blp = Blueprint("Users", "users", description="Operations on users")

@blp.route("/logout")
class UserLogout(MethodView):
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"message": "Successfully logged out"}, 200

@blp.route("/register")
class UserRegister(MethodView):
    
    @blp.arguments(UserSchema)
    def post(self, user_data):
        if UserModel.query.filter(UserModel.email == user_data["email"]).first():
            abort(409, message="A user with that email already exists.")

        user = UserModel(
            email=user_data["email"],
            password=pbkdf2_sha256.hash(user_data["password"]),
        )
        db.session.add(user)
        db.session.commit()
        
        send_simple_message(
            to=user.email,
            subject="Successfully signed up",
            body="Hi ! You have successfully signed up to Blasti. Please read the manual on our GITHUB platform to guide through our API."
        )

        return {"message": "User created successfully."}, 201
  
@blp.route("/user/<int:user_id>")
class User(MethodView):

    @blp.response(200, UserSchema)
    @jwt_required()
    def get(self, user_id):
        jwt = get_jwt()
        if not jwt.get("is_admin"):
            abort(401, message="Admin privilege required.")
             
        user = UserModel.query.get_or_404(user_id)
        return user
    
    @jwt_required()
    def delete(self, user_id):
        jwt = get_jwt()
        if not jwt.get("is_admin"):
            abort(401, message="Admin privilege required.") 
            
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted."}, 200
    
@blp.route("/login")
class UserLogin(MethodView):
    
    @blp.arguments(UserSchema)
    def post(self, user_data):        
        user = UserModel.query.filter(
            UserModel.email == user_data["email"]).first()

        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            access_token = create_access_token(identity=user.id)
            return {"access_token": access_token}, 200

        abort(401, message="Invalid credentials.")

@blp.route("/user")
class User_v(MethodView):
    @blp.response(200, UserSchema(many=True))
    @jwt_required()
    def get(self):
        jwt = get_jwt()
        if not jwt.get("is_admin"):
            abort(401, message="Admin privilege required.")
        return UserModel.query.all()
       
def send_simple_message(to,subject,body):
    domain = os.getenv("MAILGUN_DOMAIN")
    return requests.post(
		f"https://api.mailgun.net/v3/{domain}/messages",
		auth=("api", os.getenv("MAILGUN_API_KEY")),
		data={"from": "Blasti <Blasti-TN@business.tn>","to": [to],"subject": subject,"text": body})
    
