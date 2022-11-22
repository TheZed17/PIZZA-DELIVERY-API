from pydantic import BaseModel
from typing import Optional


class SignUpModel(BaseModel):
    id: Optional[int]
    username: str
    email: str
    password: str
    is_staff: Optional[bool]
    is_active: Optional[bool]

    class Config:
        orm_mode = True
        schema_extra = {
            'example': {
                'username': 'ihor',
                'email': 'ihordem@gmail.com',
                'password': 'password',
                'is_staff': False,
                'is_active': True
            }
        }


class Settings(BaseModel):
    authjwt_sercet_key: str = '812a90677415be822e42bef93a1a0d89662cf25d7332704d05ad729be00de324'


class LoginModel(BaseModel):
    username: str
    password: str


class OrderModel(BaseModel):
    id: Optional[int]
    quantity: int
    order_status: Optional[str] = 'PENDING'
    pizza_size: Optional[str] = 'SMALL'
    user_id: Optional[int]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "quantity": 2,
                "pizza_size": "LARGE"
            }
        }


class OrderStatusModel(BaseModel):
    order_status: Optional[str] = "PENDING"

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "order_status": "PENDING",
            }
        }
