"""Routes for Products App."""

from fastapi import APIRouter, Query, HTTPException

from app.utils.helpers import load_json
from .schemas import ProductMinimal, ProductPaginated

router = APIRouter()


@router.get(
    "/products",
    response_model=ProductPaginated,
    tags=["Products"],
)
async def get_products(
    page: int = Query(1, gt=0),
):
    products_data = load_json("app/data/products.json")
    page_size = 10
    start = (page - 1) * page_size
    end = start + page_size

    products = [ProductMinimal(**item) for item in products_data]
    page_products = products[start:end]
    count = len(products)
    next_page = (
        f"http://127.0.0.1:8100/api/products?page={page + 1}" if end < count else None
    )
    previous_page = (
        f"http://127.0.0.1:8100/api/products?page={page - 1}" if page > 1 else None
    )

    return {
        "count": count,
        "next": next_page,
        "previous": previous_page,
        "results": page_products,
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
