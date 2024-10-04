"""Routes for Products App."""

from typing import List, Optional
from fastapi import APIRouter, Query, HTTPException

from app.utils.helpers import load_json
from .schemas import Brand, Category, ProductMinimal, ProductPaginated
from .choices import SortChoices

router = APIRouter()


@router.get(
    "/brands",
    response_model=List[Brand],
    tags=["Products"],
)
async def get_brands():
    brands_data = load_json("app/data/brands.json")
    return brands_data


@router.get(
    "/categories",
    response_model=List[Category],
    tags=["Products"],
)
async def get_categories():
    categories_data = load_json("app/data/categories.json")
    return categories_data


@router.get(
    "/products",
    response_model=ProductPaginated,
    tags=["Products"],
)
async def get_products(
    sort_by: Optional[str] = Query(
        None,
        enum=[
            SortChoices.LATEST,
            SortChoices.OLDEST,
            SortChoices.HIGHEST_PRICE,
            SortChoices.LOWEST_PRICE,
        ],
    ),
    search: Optional[str] = Query(None),
    brand: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    page: int = Query(1, gt=0),
):
    products_data = load_json("app/data/products.json")

    # Sort_by filter
    # ! TODO: Fix id by created_at field
    if sort_by == SortChoices.LATEST:
        products_data = sorted(products_data, key=lambda x: x["id"], reverse=True)
    elif sort_by == SortChoices.OLDEST:
        products_data = sorted(products_data, key=lambda x: x["id"])
    elif sort_by == SortChoices.HIGHEST_PRICE:
        products_data = sorted(
            products_data, key=lambda x: float(x["price"]), reverse=True
        )
    elif sort_by == SortChoices.LOWEST_PRICE:
        products_data = sorted(products_data, key=lambda x: float(x["price"]))

    # Search filter
    if search:
        products_data = [
            item for item in products_data if search.lower() in item["name"].lower()
        ]

    # Brand filter
    if brand:
        products_data = [
            item for item in products_data if item["brand"].lower() == brand.lower()
        ]

    # Category filter
    if category:
        products_data = [
            item
            for item in products_data
            if item["category"].lower() == category.lower()
        ]

    products = [ProductMinimal(**item) for item in products_data]
    BASE_URL = "http://127.0.0.1:8100/api/"  # TODO: Add .env

    # Pagination
    page_size = 10
    start = (page - 1) * page_size
    end = start + page_size
    results = products[start:end]
    count = len(products)

    next_page = f"{BASE_URL}products?page={page + 1}" if end < count else None
    previous_page = f"{BASE_URL}products?page={page - 1}" if page > 1 else None

    return {
        "count": count,
        "next": next_page,
        "previous": previous_page,
        "results": results,
    }


@router.get(
    "/products/{slug}",
    response_model=ProductMinimal,
    tags=["Products"],
)
async def get_product_by_slug(slug: str):
    product_data = load_json("app/data/products.json")
    product = next(
        (product for product in product_data if product["slug"] == slug),
        None,
    )
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
