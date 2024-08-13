from marshmallow import Schema, ValidationError, fields, post_load, validates_schema
from app.models.sale import Sale, SaleDetail
from datetime import date
from app.utils.typing import SalesFilters


class SaleSchema(Schema):
    class Meta:
        model = Sale

    id = fields.Int(dump_only=True)
    sale_date = fields.DateTime(format="%Y-%m-%d %H:%M:%S", dump_only=True)
    total_amount = fields.Float(required=True)
    customer_id = fields.Int(required=True)
    sale_details = fields.List(
        fields.Nested("SaleDetailSchema"), required=False, many=True
    )

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


class SalesListFiltersSchema(Schema):
    start_date = fields.Date(required=False)
    end_date = fields.Date(required=False)

    @validates_schema
    def validate_schema(self, data, **_):
        self.validate_dates(data["start_date"], data["end_date"])

    # validations
    @staticmethod
    def validate_dates(start_date: date, end_date: date):
        if start_date and not start_date <= end_date:
            raise ValidationError("Start date must be earlier than end date.")

    @post_load
    def make_filters_object(self, data, **_) -> SalesFilters:
        return SalesFilters(**data)
