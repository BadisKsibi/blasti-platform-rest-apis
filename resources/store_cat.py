from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import Store_catModel

import itertools
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from flask_jwt_extended import jwt_required, get_jwt

from schemas import Store_catSchema
from schemas import Store_catUpdateSchema

id_iter = itertools.count()

blp = Blueprint("stores_cat", __name__, description="Operations on stores categories")

#requests that use id
@blp.route("/store_cat/<string:store_cat_id>")
class Store_cat(MethodView):
    
    @blp.response(200,Store_catSchema)
    @jwt_required()
    def get(self, store_cat_id):
        store = Store_catModel.query.get_or_404(store_cat_id)
        return store
    
    @jwt_required()
    def delete(self, store_cat_id):
        jwt = get_jwt()
        if not jwt.get("is_admin"):
            abort(401, message="Admin privilege required.")
                    
        store_cat = Store_catModel.query.get_or_404(store_cat_id)
        db.session.delete(store_cat)
        db.session.commit()
        return {"message": "Store category deleted."}

#requests that don't use id        
@blp.route("/store_cat")
class StoreList(MethodView):
    
    
    @blp.arguments(Store_catSchema)
    @blp.response(201,Store_catSchema)
    @jwt_required() 
    def post(self, store_cat_data):
        jwt = get_jwt()
        if not jwt.get("is_admin"):
            abort(401, message="Admin privilege required.")

        store_cat = Store_catModel(**store_cat_data)
        try:
            db.session.add(store_cat)
            db.session.commit()
        except IntegrityError:
            abort(400,message="A store category with that name already exists.",)
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the store.")
    
        return store_cat
   
    
    @blp.response(200, Store_catSchema(many=True))
    @jwt_required()
    def get(self):
        return Store_catModel.query.all()
            
