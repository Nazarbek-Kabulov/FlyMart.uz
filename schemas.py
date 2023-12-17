from pydantic import BaseModel, Field
from typing import List
from datetime import datetime


class AddProductSchema(BaseModel):
    name: str
    about: str = Field(..., max_length=3000)
    description: str = Field(..., max_length=3000)
    price: float
    discount_percent: float
    brand_id: int
    vendor_id: int
    status_id: int
    category_id: int
    subcategory_id: int
    category: str
    # image: str


class AllProductSchema(BaseModel):
    id: int
    name: str
    about: str
    description: str
    price: float
    discount_percent: float
    brand: dict
    vendor: dict
    status: dict
    category: dict
    subcategory: dict


class BVSchema(BaseModel):
    name: str
    # image: str


class StatusSchema(BaseModel):
    name: str
