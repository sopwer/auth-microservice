from typing import Optional

from fastapi_users import models
from pydantic import validator


class User(models.BaseUser):
    fullname: Optional[str] = None


class UserCreate(models.BaseUserCreate):
    fullname: Optional[str] = None
    password2: str

    @validator('password')
    def valid_password(cls, pass1: str):
        if len(pass1) < 10:
            raise ValueError('Password should be at least 10 characters')
        return pass1

    @validator('password2')
    def password_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError('Password doesn\'t match')
        return v


class UserUpdate(User, models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB):
    pass
