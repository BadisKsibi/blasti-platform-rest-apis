from sqlalchemy.exc import SQLAlchemyError


from db import db
from models import ItemModel

from flask_jwt_extended import jwt_required, get_jwt

from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("Items", "items", description="Operations on items")

#requests that use id
@blp.route("/item/<string:item_id>")
class Item(MethodView):
    
    @blp.response(200, ItemSchema)
    @jwt_required()
    def get(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        return item       
    
    @jwt_required()
    def delete(self, item_id):
        jwt = get_jwt()
        if not jwt.get("is_admin"):
            abort(401, message="Admin privilege required.") 
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Item deleted."}
    
    
    @blp.arguments(ItemUpdateSchema)
    @blp.response(202, ItemSchema)
    @jwt_required()      
    def put(self,item_data,item_id):        
        jwt = get_jwt()
        if not jwt.get("is_admin"):
            abort(401, message="Admin privilege required.")
        
        item = ItemModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = ItemModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()
        return item

#requests that don't use id
@blp.route("/item")
class ItemList(MethodView):
    
    @blp.response(200, ItemSchema(many=True))
    @jwt_required()
    def get(self):
        return ItemModel.query.all()
    
    
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    @jwt_required()
    def post(self, item_data):
        
        jwt = get_jwt()
        if not jwt.get("is_admin"):
            abort(401, message="Admin privilege required.")        
        
        item = ItemModel(**item_data)

        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the item.")

        return item, 201