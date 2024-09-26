"""Routes for Company App."""

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from .schemas import Applicant

router = APIRouter()


@router.post("/applicants", status_code=status.HTTP_201_CREATED)
async def create_applicant(applicant: Applicant):
    try:
        return JSONResponse(
            content={"detail": "Application created successfully."},
            status_code=status.HTTP_201_CREATED,
        )

    except ValidationError as e:
        return JSONResponse(
            content={"errors": e.errors()},
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    except Exception as e:
        return JSONResponse(
            content={"errors": f"An error occurred: {e}"},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
