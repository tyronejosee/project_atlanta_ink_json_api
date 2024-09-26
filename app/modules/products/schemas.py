"""Schemas for Artists App."""

from typing import List, Optional
from pydantic import BaseModel


class Brand(BaseModel):

    id: str
    name: str


class Category(BaseModel):

    id: str
    name: str


class Product(BaseModel):

    id: str
    name: str
    slug: str
    sku: str
    description: str
    price: str
    brand: str
    currency: str
    image: str
    category: str
    stock: int
    is_featured: bool
    created_at: str
    updated_at: str


class ProductMinimal(BaseModel):

    id: str
    name: str
    slug: str
    price: str
    brand: str
    image: str
    category: str


class ProductPaginated(BaseModel):

    count: int
    next: Optional[str]
    previous: Optional[str]
    results: List[ProductMinimal]
