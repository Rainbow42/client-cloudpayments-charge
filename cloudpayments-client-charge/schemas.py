import re
from functools import partial

from marshmallow import Schema, fields


class PascalCasedSchema(Schema):
    """
    CloudPayment принимает ключи в теле запроса в стиле PascalCase,
    поэтому наименование полей переводим в требуемый стиль
    """

    def on_bind_field(self, field_name, field_obj):
        field_names = field_name.split('_')
        field = str()
        for name in field_names:
            chr_ = name[0].upper() + name[1:]
            field += chr_
        field_obj.data_key = field


class ChargePaySchema(PascalCasedSchema):
    amount = fields.Float(required=True)
    currency = fields.Str(required=False)
    description = fields.Str(required=False)
    ip_address = fields.Str(required=False)
    card_cryptogram_packet = fields.Str(required=True)
    name = fields.Str(required=False)
    payment_url = fields.URL(required=False)
    invoice_id = fields.Str(required=False)
    culture_name = fields.Str(required=False)
    account_id = fields.Str(required=False)
    email = fields.Str(required=False)
    payer = fields.Dict(required=False)
    json_data = fields.Dict(
        keys=fields.Str(),
        values=fields.Str(),
        required=False,
        data_key="JsonData",
    )
