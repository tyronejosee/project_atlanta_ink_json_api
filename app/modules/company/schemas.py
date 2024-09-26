"""Schemas for Company App."""

from pydantic import BaseModel


class Company(BaseModel):

    name: str
    description: str
    instagram: str
    youtube: str
    twitch: str
    tiktok: str
    whatsapp: str
    rights: str
    location: str


class Price(BaseModel):

    id: str
    name: str
    description: str
    price_range: str
    is_featured: bool


class Service(BaseModel):

    id: str
    name: str
    image: str
    description: str


class Faq(BaseModel):

    id: str
    question: str
    answer: str
