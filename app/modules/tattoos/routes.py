"""Routes for Tattoos App."""

from typing import List
from fastapi import APIRouter

from app.utils.helpers import load_json
from .schemas import Tattoo

router = APIRouter()


@router.get(
    "/tattoos",
    response_model=List[Tattoo],
    tags=["Tattoos"],
)
async def get_tattoos():
    tattoos_data = load_json("app/data/tattoos.json")
    return tattoos_data
