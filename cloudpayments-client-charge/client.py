import base64
from typing import Any

from abstract_client import AbstractInteractionClient
from aiohttp import TCPConnector
from authentication import AuthenticationHTTP
from schemas import ChargePaySchema
from urls import CLOUD_PAYMENTS, PaymentCryptogramApi


class PaymentsError(Exception):
    def __init__(self, response):
        self.response = response
        super().__init__(response.get('Message'))


class ProcessPay(AbstractInteractionClient):
    """Проведение платежей"""
    charge_pay_schema = ChargePaySchema()
    base_auth = AuthenticationHTTP()

    BASE_URL = CLOUD_PAYMENTS
    SERVICE = 'CLOUD_PAYMENTS'
    CONNECTOR = TCPConnector(verify_ssl=False)

    def __init__(self, public_id: str, api_secret: str):
        """
        :param public_id: выдается в личном кабинете платежной системы (используется как логин для аутентификации)
        :param api_secret: выдается в личном кабинете платежной системы (используется как пароль для аутентификации)
        """
        super().__init__()
        self.public_id = public_id
        self.api_secret = api_secret

    def _auth_make_headers(self, request_id: str = None, headers: dict = None) -> dict:
        """Добавление в заголовок стандартной аутентификации HTTP Basic Auth"""
        if headers is None:
            headers = dict(headers={})

        headers["headers"].update({'Authorization-Type': self.base_auth(self.public_id, self.api_secret)})
        if request_id is not None:
            headers['X-Request-ID'] = request_id

        return headers

    @staticmethod
    def _headers_make(headers: dict = None) -> dict:
        if headers is None:
            headers = dict(headers={})
        headers["headers"].update({'Content-Type': 'application/json'})
        return headers

    async def charge_pay(
        self,
        ip_address: str,
        amount: float,
        card_cryptogram_packet: str,
        currency: str = 'RUB',
        **kwargs: Any
    ):
        """Проведение одностадийного платежа(charge) c использованием токена YandexPay
        :param currency:  необязательный параметр -  Валюта
        :param ip_address: обязательный параметр -  IP-адрес плательщика
        :param amount: обязательный параметр -  Сумма платежа
        :param card_cryptogram_packet: обязательный параметр - Сервис Yandex Pay создает платежный токен
        """
        # ToDo добавить обработку ответов от сервера (в случае если успешный, ошибка или оплата через Secure3d)
        params = {
            "ip_address": ip_address,
            "amount": amount,
            "card_cryptogram_packet": base64.b64decode(card_cryptogram_packet),
            "currency": currency
        }
        body_charge_pay = {"json": self.charge_pay_schema.dump(params)}
        charge_url = self.endpoint_url(PaymentCryptogramApi.charge_pay)

        headers = self._auth_make_headers(headers=self._headers_make())

        data = {**body_charge_pay, **headers}
        response = await self.post("POST", charge_url, **data)

        await self.close()
        if response.get('Success') and response.get('Model', {}).get("ReasonCode") == 0:
            #   транзакция принята
            return response
        if response.get('Success') is False and response['Message'] and response.get('Model'):
            # требуется 3-D Secure аутентификация
            return response
        if response.get('Model', {}).get("ReasonCode", {}) != 0:
            #  транзакция отклонена
            raise PaymentsError(response)
        if response.get('Message') is None:
            #  транзакция отклонена
            raise PaymentsError(response)
