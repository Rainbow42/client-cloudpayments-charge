from typing import Any
from schemas import ChargePaySchema
from urls import PaymentCryptogramApi, CLOUD_PAYMENTS
from authentication import AuthenticationHTTP

from abstract_client import AbstractInteractionClient


class YandexPay(AbstractInteractionClient):
    def get_access_token(self):
        # ToDo реализовать получение токена из YandexPay
        pass


class AuthenticationPay(AbstractInteractionClient):
    """Аутентификация платежей"""
    charge_pay_schema = ChargePaySchema()
    base_auth = AuthenticationHTTP()

    BASE_URL = CLOUD_PAYMENTS

    def __init__(self, public_id: str, api_secret: str, merchant_id: str = None):
        """
            :param public_id: выдается в личном кабинете платежной системы (используется как логин для аутентификации)
            :param api_secret: выдается в личном кабинете платежной системы (используется как пароль для аутентификации)
            :param merchant_id: выдается Yandex Pay
        """
        super().__init__()

        self.public_id = public_id
        self.api_secret = api_secret
        self.merchant_id = merchant_id

    def _auth_make(self, request_id: str = None) -> dict:
        headers = {'Authorization': self.base_auth(self.public_id, self.api_secret)}
        if request_id is not None:
            headers['X-Request-ID'] = request_id
        return headers

    async def charge_pay(
            self,
            ip_address: str,
            amount: float,
            card_cryptogram_packet: str,
            currency: str = 'RUB',
            **kwargs: Any
    ):
        # ToDo добавить обработку ответов от сервера (в случае если успешный, ошибка или оплата через Secure3d)
        params = {
            "ip_address": ip_address,
            "amount": amount,
            "card_cryptogram_packet": card_cryptogram_packet,
            "currency": currency
        }
        body_charge_pay = self.charge_pay_schema.load(params.update(kwargs))
        charge_url = self.endpoint_url(PaymentCryptogramApi.charge_pay)
        headers = self._auth_make()

        response = await self.post(body_charge_pay, charge_url, headers)
        await self.close()
        return response
