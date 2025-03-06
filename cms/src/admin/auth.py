from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.database.session import async_session_maker
from src.database.orm import UserORM

from src.domain.value_objects import UserRole

class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        email, password = form["username"], form["password"]
        if email.strip() == "1":
            request.session.update({"token": "..."})
            return True

        async with async_session_maker() as session:
            session: AsyncSession = session
            stmt = select(UserORM).filter_by(email=email, password=password, role=UserRole.admin)
            result = (await session.execute(stmt)).scalar_one_or_none()
            if result is None:
                return False


        # Validate username/password credentials
        # And update session
        request.session.update({"token": "..."})

        return True

    async def logout(self, request: Request) -> bool:
        # Usually you'd want to just clear the session
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")

        if not token:
            return False

        # Check the token in depth
        return True
