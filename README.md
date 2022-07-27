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

- Реализована аутентификация `HTTP Basic Auth` для запросов к CloudPayments в классе `AuthenticationHTTP` 
- Реализованы юнит-тесты 