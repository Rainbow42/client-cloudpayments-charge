import base64
from unittest import IsolatedAsyncioTestCase, mock
from uuid import uuid4

from client import ProcessPay
from parameterized import parameterized

from .fixtures import FIXTURES_RESPONSE_ACCEPT, FIXTURES_RESPONSE_REJECTED


class PaymentTestCase(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.public_id, self.api_secret = str(uuid4()), str(uuid4())
        self.payment_token = base64.b64encode(bytes(str(uuid4()), 'utf-8'))

    @parameterized.expand([
        ({"Success": False, "Message": "Amount is required"},),
        (FIXTURES_RESPONSE_REJECTED,)
    ])
    async def test_rejected_transaction(self, test_response):
        request_path = mock.patch(
            "abstract_client.AbstractInteractionClient._request",
            mock.AsyncMock(return_value=test_response)
        )

        with request_path as _:
            pay = ProcessPay(self.public_id, self.api_secret)
            with self.assertRaises(Exception) as error:
                await pay.charge_pay(
                    ip_address=str(uuid4()),
                    amount=100,
                    card_cryptogram_packet=self.payment_token.decode("ascii"),
                )
            exception = error.exception
            self.assertEqual(test_response["Message"], exception.response.get("Message"))

    @parameterized.expand([
        (FIXTURES_RESPONSE_ACCEPT,)
    ])
    async def test_accepted_transaction(self, test_response):
        request_path = mock.patch("abstract_client.AbstractInteractionClient._request",
                                  mock.AsyncMock(return_value=test_response))

        with request_path as _:
            pay = ProcessPay(self.public_id, self.api_secret)
            response = await pay.charge_pay(
                    ip_address=str(uuid4()),
                    amount=100,
                    card_cryptogram_packet=self.payment_token.decode("ascii")
            )
            self.assertEqual(test_response, response)
