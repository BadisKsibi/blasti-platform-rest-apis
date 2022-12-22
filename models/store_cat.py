from db import db


class Store_catModel(db.Model):
    __tablename__ = "store_cat"

    id = db.Column(db.Integer, primary_key=True)
    store_cat = db.Column(db.String(80), unique=True, nullable=False)
    items = db.relationship("ItemModel", back_populates="store_cat", lazy="dynamic", cascade="all, delete")