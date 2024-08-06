from datetime import date
from typing import Optional
from uuid import UUID
from beanie import Link
from pydantic import BaseModel, EmailStr, Field

from models.role_model import Role


class UserAuth(BaseModel):
    email: EmailStr = Field(..., description="User's email.")
    password: str = Field(..., min_length=4, max_length=25, description="User's password.")
    name: str = Field(..., min_length=3, max_length=50, description="User's name.")
    gender: str = Field(..., description="User's gender.")
    phone: Optional[int] = Field(None, description="User's phone number.")
    birthday: Optional[date] = Field(None, description="User's birthday.")
    status: bool = Field(default=True, description="User's status.")
    street_name: Optional[str] = Field(None, description="User's street name.")
    street_number: Optional[str] = Field(None, description="User's street number.")
    zip_code: Optional[int] = Field(None, description="User's zip code.")
    role: Optional[Link[Role]] = Field(None, description="User's role.")
    colony: Optional[str] = Field(None, description="User's colony.")
    city: Optional[str] = Field(None, description="User's city.")
    country: Optional[str] = Field(None, description="User's country.")
    user_type: Optional[str] = Field(None, description="User's type.")

    class Settings:
        collection = "users"

    class Config:
        schema_extra = {
            "example": {
                "email": "user@example.com",
                "password": "securepass123",
                "name": "John Doe",
                "gender": "Male",
                "phone": 1234567890,
                "birthday": "1990-01-01",
                "status": True,
                "street_name": "Main St",
                "street_number": "123",
                "zip_code": 12345,
                "role": "65d662f3751e027f07175ae0",  # This would be the ObjectId of a Role document
                "colony": "Center",
                "city": "City",
                "country": "Country",
                "user_type": "Admin"
            }
        }


class UserOut(BaseModel):
    user_id: UUID
    hashed_password: str
    email: EmailStr
    name: str
    phone: Optional[int]
    gender: str
    age: int
    username: str
    role: Optional[Link[Role]]
    status: Optional[bool]
    avatar: Optional[str]
    user_type: str
    user_count: str


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = Field(description="User's email.")
    name: Optional[str] = Field(description="User's name.")
    role: Optional[Link[Role]]
    gender: Optional[str]
    phone: Optional[int]
    birthday: Optional[str]
    address: Optional[str]
    status: Optional[bool]
    avatar: Optional[str]
    age: Optional[int]
