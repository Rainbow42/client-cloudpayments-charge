from marshmallow_dataclass import dataclass


CLOUD_PAYMENTS = 'https://api.cloudpayments.ru'


@dataclass
class PaymentCryptogramApi:
    charge_pay = '/payments/cards/charge/'
