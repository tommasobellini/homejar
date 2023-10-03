from typing import Optional
import uuid
from pydantic import BaseModel, Field


class HomeJarModel(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    active: bool = False
    created_at: Optional[str] = None
    created_by: Optional[str] = None
    modified_at: Optional[str] = None
    modified_by: Optional[str] = None


class ListUser(HomeJarModel):
    username: str
    email: Optional[str] = None
