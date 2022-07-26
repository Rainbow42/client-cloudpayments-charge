from base64 import b64encode
from typing import Any


class AuthenticationHTTP:

    @staticmethod
    def __str_decode(str_: Any, encoding: str = "ascii") -> str:
        if isinstance(str_, str):
            return str_
        return str_.decode(encoding)

    def __call__(self, username: str, password: str):
        if isinstance(username, str):
            username = username.encode("latin1")

        if isinstance(password, str):
            password = password.encode("latin1")

        auth = self.__str_decode(
            b64encode(b":".join((username, password))).strip()
        )

        return "Basic " + auth
