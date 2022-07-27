from dataclasses import dataclass

CLOUD_PAYMENTS = 'https://api.cloudpayments.ru'


@dataclass
class PaymentCryptogramApi:
    charge_pay = '/payments/cards/charge/'
