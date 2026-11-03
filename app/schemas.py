from datetime import datetime
from uuid import UUID
from fastapi_users import schemas

from pydantic import BaseModel, ConfigDict


class PostResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    user_id: UUID
    caption: str
    url: str
    file_type: str
    file_name: str
    created_at: datetime


class PostCreate(BaseModel):
    caption: str = ""


class UserRead(schemas.BaseUser[UUID]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass
