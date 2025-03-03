from datetime import datetime, timezone
from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from src.backend.adapters.authorization import AccessToken

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="authenticaition")


async def provide_access_token(
    encoded_token: Annotated[str, Depends(oauth2_scheme)],
) -> AccessToken:
    return AccessToken.decode(encoded_token)
