"""Schemas for Tattoos App."""

from pydantic import BaseModel


class Tattoo(BaseModel):

    id: str
    name: str
    slug: str
    image: str
    artist: str
