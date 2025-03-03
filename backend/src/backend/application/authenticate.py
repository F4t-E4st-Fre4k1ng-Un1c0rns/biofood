from datetime import datetime, timedelta, timezone
from enum import StrEnum

from src.backend.adapters.authorization import AccessToken
from src.backend.application.common.interactor import Interactor
from src.backend.application.common.oauth import YandexID
from src.backend.application.common.uow import UoW
from src.backend.domain.common import Base
from src.backend.domain.exceptions import NotFound
from src.backend.domain.models import User
from src.backend.domain.value_objects import UserRole


class OauthMethods(StrEnum):
    yandex_id = "yandexId"


class AuthenticateDTO(Base):
    oauth_token: str
    oauth_method: OauthMethods


class AuthenticateResultDTO(Base):
    user: User
    access_token: str
    expiration_time: datetime


class Authenticate(Interactor[AuthenticateDTO, AuthenticateResultDTO]):
    def __init__(self, uow: UoW, yandex_id: YandexID) -> None:
        self.uow = uow
        self.yandex_id = yandex_id

    async def __call__(self, data: AuthenticateDTO) -> AuthenticateResultDTO:
        email = await self.__fetch_email(data.oauth_method, data.oauth_token)
        user = await self.__find_user_by_email(email)
        token = self.__create_access_token(user)
        return AuthenticateResultDTO(
            user=user, access_token=token.encode(), expiration_time=token.exp
        )

    async def __fetch_email(self, oauth_method: OauthMethods, oauth_token: str):
        match oauth_method:
            case OauthMethods.yandex_id:
                email = await self.yandex_id.fetch_user_email(oauth_token)
        return email

    async def __find_user_by_email(self, email) -> User:
        async with self.uow:
            by_filter = {"email": email}
            try:
                user = await self.uow.user.find_one(by_filter=by_filter)
            except NotFound:
                model_data = {"role": UserRole.client, "email": email}
                user = await self.uow.user.create_one(model_data)
                await self.uow.commit()
        return user

    def __create_access_token(self, user):
        return AccessToken(
            exp=datetime.now(timezone.utc) + timedelta(days=1),
            user_id=user.id,
            user_role=user.role,
        )
