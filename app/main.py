"""Main configs."""

import os
import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request

from app.core.config import settings
from app.modules.applicants import routes as applicants
from app.modules.artists import routes as artists
from app.modules.bookings import routes as bookings
from app.modules.company import routes as company
from app.modules.products import routes as products
from app.modules.tattoos import routes as tattoos


# API Metadata
tags_metadata = [
    {
        "name": "Artists",
        "description": "Operations related to Artists",
    },
    {
        "name": "Tattoos",
        "description": "Operations related to Tattoos",
    },
    {
        "name": "Company",
        "description": "Operations related to Company",
    },
]

# Initialize FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    summary="A JSON API created for the Coding Latam community.",
    description=("\nAccess the API documentation at `/docs` or `/redoc`."),
    version=str(os.environ.get("API_VERSION")),
    # terms_of_service="http://example.com/terms/",
    contact={
        "name": "Coding Latam GitHub",
        "url": "https://github.com/Coding-Latam",
    },
    license_info={
        "name": "MIT License",
        "url": "https://github.com/tyronejosee/",
    },
    debug=False,
    openapi_tags=tags_metadata,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


# Redirect root to documentation
@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")


# Redirect to the documentation if the page is not found
@app.exception_handler(404)
async def not_found_error(request: Request, exc: Exception):
    return RedirectResponse(url="/docs")


# Include routers
app.include_router(applicants.router, prefix=settings.API_V1_STR)
app.include_router(artists.router, prefix=settings.API_V1_STR)
app.include_router(bookings.router, prefix=settings.API_V1_STR)
app.include_router(company.router, prefix=settings.API_V1_STR)
app.include_router(products.router, prefix=settings.API_V1_STR)
app.include_router(tattoos.router, prefix=settings.API_V1_STR)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
