from marshmallow import Schema, fields, post_load
from app.models.sale import Sale, SaleDetail

class SaleSchema(Schema):
    class Meta:
        model = Sale

    id = fields.Int(dump_only=True)
    sale_date = fields.DateTime(format='%Y-%m-%d %H:%M:%S', dump_only=True)
    total_amount = fields.Float(required=True)
    customer_id = fields.Int(required=True)
    sale_details = fields.List(fields.Nested("SaleDetailSchema"), required=False, many=True)

    @post_load
    def make_sale(self, data, **_) -> Sale:
        return Sale(**data)

class SaleDetailSchema(Schema):
    class Meta:
        model = SaleDetail

    id = fields.Int(dump_only=True)
    sale_id = fields.Int(load_only=True)
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True)
    price_at_sale = fields.Float(required=True)

    @post_load
    def make_sale_detail(self, data, **_) -> SaleDetail:
        return SaleDetail(**data)
