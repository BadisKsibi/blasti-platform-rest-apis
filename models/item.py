from db import db


class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)
    store_cat_id = db.Column(db.Integer, db.ForeignKey("store_cat.id"), unique=False, nullable=False)
    store_cat = db.relationship("Store_catModel", back_populates="items")