"""Schemas for Artists App."""

from typing import List

from app.utils.mixins import BaseSchema


class Style(BaseSchema):

    name: str


class Artist(BaseSchema):

    name: str
    image: str
    instagram: str
    whatsapp: str
    description: str
    slug: str
    styles: List[Style]
    is_team: bool
