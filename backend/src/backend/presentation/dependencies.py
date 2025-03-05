from datetime import datetime, timezone
from typing import Annotated

from backend.domain.exceptions import AuthorizationError
from backend.domain.value_objects import UserRole
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from src.backend.adapters.authorization import AccessToken

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="authenticaition")


async def provide_access_token(
    encoded_token: Annotated[str, Depends(oauth2_scheme)],
) -> AccessToken:
    return AccessToken.decode(encoded_token)

async def provide_admin_access_token(
    encoded_token: Annotated[str, Depends(oauth2_scheme)],
) -> AccessToken:
    token = AccessToken.decode(encoded_token)
    if token.user_role == UserRole.client:
        raise AuthorizationError("You have to be staff to access this endpoint")
    return token
