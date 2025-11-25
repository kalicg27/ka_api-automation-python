from pydantic import BaseModel


class User(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class CreateUserRequest(BaseModel):
    name: str
    job: str


class CreateUserResponse(BaseModel):
    name: str
    job: str
    id: str
    createdAt: str
