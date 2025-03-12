from collections.abc import Sequence
from typing import Optional

from pydantic import Field, RootModel

from backend.application.common.authorization import AccessTokenI
from src.backend.application.common.interactor import Interactor
from src.backend.application.common.uow import UoW
from src.backend.domain.common import Base as DomainModelBase
from src.backend.domain.exceptions import NotFound
from src.backend.domain.models import PushSubscriptionID


class PushSubscriptionInputDTO(DomainModelBase):
    id: Optional[PushSubscriptionID]
    endpoint: str
    p256dh: str
    auth: str

class PushSubscriptionOutputDTO(DomainModelBase):
    id: PushSubscriptionID

class AddPushSubscription(
    Interactor[PushSubscriptionInputDTO, PushSubscriptionOutputDTO]
):
    def __init__(self, uow: UoW, token: AccessTokenI):
        self.uow = uow
        self.token = token

    async def __call__(
        self, data: PushSubscriptionInputDTO
    ) -> PushSubscriptionOutputDTO:
        async with self.uow:
            record_id = await self.__subscribe(data)
            await self.uow.commit()
        return PushSubscriptionOutputDTO(id=record_id)

    async def __subscribe(self, input: PushSubscriptionInputDTO):
        try:
            return await self.__update_subscription(input)
        except NotFound:
            return await self.__create_subscription(input)
    
    async def __update_subscription(self, input: PushSubscriptionInputDTO):
        data = {
            "user_id": self.token.user_id,
            "endpoint": input.endpoint,
            "p256dh": input.p256dh,
            "auth": input.auth,
        }
        record = await self.uow.push_subscription.update_one(id=input.id, data=data)
        return record.id

    async def __create_subscription(self, input: PushSubscriptionInputDTO):
        data = {
            "user_id": self.token.user_id,
            "endpoint": input.endpoint,
            "p256dh": input.p256dh,
            "auth": input.auth
        }
        record = await self.uow.push_subscription.create_one(data)
        return record.id

