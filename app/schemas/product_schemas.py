from marshmallow import Schema, fields, post_load
from app.models.product import Product

class ProductSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    stock_quantity = fields.Int(required=True)
    description = fields.Str(required=False)
    barcode = fields.Str(required=True)

    @post_load
    def make_product(self, data, **_):
        return Product(**data)
