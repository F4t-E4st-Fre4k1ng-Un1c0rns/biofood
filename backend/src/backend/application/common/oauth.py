from abc import abstractmethod


class YandexID:
    @abstractmethod
    async def fetch_user_email(self, tocken: str):
        raise NotImplementedError
