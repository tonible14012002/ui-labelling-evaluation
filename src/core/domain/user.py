from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

# Define the application schema here
class User(BaseModel):
    id: int = None
    name: str = ""
    email: EmailStr = ""
    activated_at: datetime
    is_superuser: bool = False
    created_at: datetime
    updated_at: datetime

class UserQuery(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    email: Optional[str] = None
    id__in: List[int] = []