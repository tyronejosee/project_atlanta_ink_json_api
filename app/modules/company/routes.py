"""Routes for Company App."""

from typing import List
from fastapi import APIRouter

from typing import Optional
from app.utils.helpers import load_json
from .schemas import Company, Price, Service, Faq

router = APIRouter()


@router.get(
    "/company",
    response_model=Company,
    tags=["Company"],
)
async def get_company_data():
    company_data = load_json("app/data/company.json")
    return company_data


@router.get(
    "/prices",
    response_model=List[Price],
    tags=["Company"],
)
async def get_prices(is_featured: Optional[bool] = None):
    prices_data = load_json("app/data/prices.json")

    if is_featured is not None:
        prices_data = [
            price for price in prices_data if price.get("is_featured") == is_featured
        ]

    return prices_data


@router.get(
    "/services",
    response_model=List[Service],
    tags=["Company"],
)
async def get_services():
    services_data = load_json("app/data/services.json")
    return services_data


@router.get(
    "/faqs",
    response_model=List[Faq],
    tags=["Company"],
)
async def get_faqs():
    faqs_data = load_json("app/data/faqs.json")
    return faqs_data
