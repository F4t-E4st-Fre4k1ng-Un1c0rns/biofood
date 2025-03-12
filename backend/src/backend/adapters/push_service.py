from io import BytesIO

from httpx import AsyncClient, HTTPStatusError
from webpush import WebPush
from webpush.types import WebPushKeys, WebPushSubscription

from src.backend.application.common.push_service import PushService
from src.backend.domain.aggregates import Order
from src.backend.domain.exceptions import AuthenticationError
from src.backend.domain.models import PushSubscription
from src.backend.settings import settings


class PushServiceGateway(PushService):
    def __init__(self):
        self.client = AsyncClient(http2=True)
        self.wp = WebPush(
            public_key=BytesIO(settings.PUBLIC_VAPID_KEY.encode()),
            private_key=BytesIO(settings.PRIVATE_VAPID_KEY.encode()),
        )

    async def send(self, updated_order: Order, subscriptions: list[PushSubscription]):
        """
        Send push notifications
        """
        async with self.client:
            for db_subscription in subscriptions:
                keys = WebPushKeys(
                    auth=db_subscription.auth, p256dh=db_subscription.p256dh
                )
                subscription = WebPushSubscription(
                    endpoint=db_subscription.endpoint, keys=keys
                )
                message = self.wp.get(
                    message=updated_order.model_dump_json(),
                    subscription=subscription,
                    subscriber=f"{db_subscription.user_id}@biofood",
                )
                await self.client.post(
                    url=str(subscription.endpoint),
                    data=message.encrypted,
                    headers=message.headers,
                )
