from fastapi import APIRouter, BackgroundTasks, status
from app.schemas import UserCreate, UserRead
from app.services import create_user, send_welcome_email
from typing import Any

router = APIRouter()

@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def register_user(user: UserCreate, background_tasks: BackgroundTasks) -> Any:
    pass
