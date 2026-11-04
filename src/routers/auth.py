from fastapi import APIRouter

from src.core.dependencies import CurrentUser
from src.db.dependencies import SessionDep
from src.repositories.user_repository import UserRepository
from src.schemas.auth import TokenResponse, UserLogin, UserRegister, UserResponse
from src.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserResponse, status_code=201)
async def register(data: UserRegister, session: SessionDep):
    return await AuthService(UserRepository(session)).register(data)


@router.post("/login", response_model=TokenResponse)
async def login(data: UserLogin, session: SessionDep):
    return await AuthService(UserRepository(session)).login(data)


@router.get("/me", response_model=UserResponse)
async def me(user: CurrentUser):
    return user
