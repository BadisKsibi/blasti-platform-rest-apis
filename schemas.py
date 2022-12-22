from marshmallow import Schema, fields
#input: required, output:dumponly
class PlainItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)

class PlainStore_catSchema(Schema):
    id = fields.Str(dump_only=True)
    store_cat = fields.Str(required=True)
    
class ItemSchema(PlainItemSchema):
    store_cat_id = fields.Int(required=True, load_only=True)
    store_cat = fields.Nested(PlainStore_catSchema(), dump_only=True)

class Store_catSchema(PlainStore_catSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)

#updates of PUT need
class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()

class Store_catUpdateSchema(Schema):
    store_cat = fields.Str()

#user
class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    
    