"""Routes for Company App."""

from fastapi import APIRouter, status, Form, UploadFile, File
from fastapi.responses import JSONResponse
from pydantic import ValidationError

router = APIRouter()


@router.post(
    "/applicants",
    status_code=status.HTTP_201_CREATED,
    tags=["Applicants"],
)
async def create_applicant(
    name: str = Form(..., min_length=5, max_length=100),
    email: str = Form(..., min_length=5, max_length=100),
    phone: str = Form(..., min_length=12, max_length=12),
    cv: UploadFile = File(None),
    message: str = Form(None),
):
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
