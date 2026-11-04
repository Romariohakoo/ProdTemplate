from fastapi import HTTPException, status

from src.core.security import create_access_token, hash_password, verify_password
from src.models.user_model import UserModel
from src.repositories.user_repository import UserRepository
from src.schemas.auth import TokenResponse, UserLogin, UserRegister


class AuthService:
    def __init__(self, users: UserRepository):
        self.users = users

    async def register(self, data: UserRegister) -> UserModel:
        if await self.users.get_by_email(data.email) is not None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered",
            )
        if await self.users.get_by_username(data.username) is not None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Username already taken",
            )
        return await self.users.create(
            username=data.username,
            email=data.email,
            hashed_password=hash_password(data.password),
        )

    async def login(self, data: UserLogin) -> TokenResponse:
        user = await self.users.get_by_email(data.email)
        if user is None or not verify_password(data.password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
            )
        return TokenResponse(access_token=create_access_token(str(user.id)))
