import re
from functools import partial

from marshmallow import Schema, fields


class CamelCasedSchema(Schema):
    """
    CloudPayment принимает ключи в теле запроса в стиле CamelCase,
    поэтому наименование полей переводим в требуемый стиль
    """
    _snake_case = re.compile(r"(?<=\w)_(\w)")
    _to_camel_case = partial(_snake_case.sub, lambda m: m[1].upper())

    def on_bind_field(self, field_name, field_obj, _cc=_to_camel_case):
        field_obj.data_key = _cc(field_name.lower())


class ChargePaySchema(CamelCasedSchema):
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
