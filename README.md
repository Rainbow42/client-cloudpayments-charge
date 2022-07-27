# client-cloudpayments-charge

Python клиент для платежного сервиса CloudPayments, работает через API CloudPayments и Yandex Pay.
Оплата должна происходить следующим способом, сначала нужно получить платежные токен через Yandex Pay Web SDK, 
этот токен API Secret и логин Public ID, с паролем должен передаваться в интерфейс клиента для проведения оплаты.

- Реализован интерфейс проведение оплат через криптограмму для одностадийного(charge) платежа
 
    `ProcessPay(public_id, api_secret).charge_pay(ip_address: str, amount: float, card_cryptogram_packet: str,
            currency: str = 'RUB')`

`ip_address`: обязательный параметр - IP-адрес плательщика

`currency`: необязательный параметр -  Валюта

`amount`: обязательный параметр - Сумма платежа

`card_cryptogram_packet`: обязательный параметр - Сервис Yandex Pay создает платежный токен плательщика, этот токен декодируются из base64 и отправляться в `CardCryptogramPacket`
Пример сформированного запроса для платежа:

``{
  "json": {
    "Currency": "RUB",
    "CardCryptogramPacket": "28cd3e9c-b98b-4f3c-a837-54cde6785a61",
    "IpAddress": "d3ce852b-9f4d-4bd0-b17e-3fac576019e0",
    "Amount": 100
  },
  "headers": {
    "Content-Type": "application/json",
    "Authorization-Type": "Basic NjNkZjkwYWItOGJkNS00N2UwLTk1N2YtMWE2OTE0NTZiMTdkOjgwNzE0MzVlLWMxYzItNDBhZC04MTZiLWQ3Yzc3YTA2NmYxZA=="
  }
}``

json - аргумент метода aiohttp, который добавляет данные в body 
headers  - аргумент метода aiohttp, который добавляет данные в HTTP Headers  
- Реализована аутентификация `HTTP Basic Auth` для запросов к CloudPayments в классе `AuthenticationHTTP` 
- Реализованы юнит-тесты 