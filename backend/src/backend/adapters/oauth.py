from httpx import AsyncClient, HTTPStatusError

from src.backend.application.common.oauth import YandexID
from src.backend.domain.exceptions import AuthenticationError


class YandexIdGateway(YandexID):
    URL = "https://login.yandex.ru/info"
    PARAMETERS = {"format": "json"}

    def __init__(self):
        self.client = AsyncClient(http2=True)

    async def fetch_user_email(self, token: str) -> str:
        """
        Fetch user email from YandexID
        """
        async with self.client:
            responce = await self.client.get(
                url=self.URL,
                params=self.PARAMETERS,
                headers={"Authorization": token},
            )
            try:
                responce.raise_for_status()
            except HTTPStatusError:
                raise AuthenticationError("YandexID token invalid")
            print(responce.json())
            return responce.json()["default_email"]
