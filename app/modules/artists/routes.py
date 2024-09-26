"""Routes for Artists App."""

from typing import List
from fastapi import APIRouter, HTTPException

from app.utils.helpers import load_json
from app.modules.tattoos.schemas import Tattoo
from .schemas import Artist

router = APIRouter()


@router.get(
    "/artists",
    response_model=List[Artist],
    tags=["Artists"],
)
async def get_artists():
    artists_data = load_json("app/data/artists.json")
    return artists_data


@router.get(
    "/artists/{slug}",
    response_model=Artist,
    tags=["Artists"],
)
async def get_artist_by_slug(slug: str):
    artists_data = load_json("app/data/artists.json")
    artist = next(
        (artist for artist in artists_data if artist["slug"] == slug),
        None,
    )
    if artist is None:
        raise HTTPException(status_code=404, detail="Artist not found")
    return artist


@router.get(
    "/artists/{slug}/tattoos",
    response_model=List[Tattoo],
    tags=["Artists"],
)
async def get_artist_tattoos(slug: str):
    artists_data = load_json("app/data/artists.json")
    tattoos_data = load_json("app/data/tattoos.json")

    valid_slugs = {artist["slug"] for artist in artists_data}
    if slug not in valid_slugs:
        raise HTTPException(
            status_code=400,
            detail="Slug not valid.",
        )

    artist = next(
        (artist for artist in artists_data if artist["slug"] == slug),
        None,
    )

    artist_name = artist["name"]

    if artist is None:
        raise HTTPException(status_code=404, detail="Artist not found")

    artist_tattoo = [item for item in tattoos_data if item["artist"] == artist_name]

    if artist_tattoo:
        return artist_tattoo
    raise HTTPException(
        status_code=404,
        detail="Tattoos not found.",
    )
