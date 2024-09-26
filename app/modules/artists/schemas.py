"""Schemas for Artists App."""

from typing import List

from pydantic import BaseModel


class Style(BaseModel):

    id: str
    name: str
    updated_at: str
    created_at: str


class Artist(BaseModel):

    id: str
    name: str
    image: str
    instagram: str
    whatsapp: str
    description: str
    slug: str
    styles: List[Style]
    is_team: bool
    updated_at: str
    created_at: str
