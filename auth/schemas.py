from _datetime import datetime

from pydantic import BaseModel, Field


class User(BaseModel):
    first_name: str
    last_name: str
    phone: str
    email: str
    gender: str
    date_of_birth: datetime
    password1: str
    password2: str


class UserInDB(BaseModel):
    first_name: str
    last_name: str
    phone: str
    email: str
    gender: str
    date_of_birth: datetime
    password: str = Field(required=False)


class UserInfo(BaseModel):
    first_name: str
    last_name: str
    gender: str
    date_of_birth: datetime
    email: str
    phone: str


class UserLogin(BaseModel):
    phone: str
    password: str
