from marshmallow import Schema, fields, post_load
from app.models.customer import Customer

class CustomerSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    contact = fields.Str(required=True)
    address = fields.Str(required=True)
    email = fields.Email(required=False)

    @post_load
    def make_customer(self, data, **_) -> Customer:
        return Customer(**data)
