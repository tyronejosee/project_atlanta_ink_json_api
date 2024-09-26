"""Routes for Bookings App."""

from fastapi import APIRouter, status, Form, UploadFile, File
from fastapi.responses import JSONResponse
from pydantic import ValidationError

router = APIRouter()


@router.post(
    "/bookings",
    status_code=status.HTTP_201_CREATED,
    tags=["Bookings"],
)
async def create_booking(
    first_name: str = Form(..., max_length=100),
    last_name: str = Form(..., max_length=100),
    phone: str = Form(..., max_length=15),
    notes: str = Form(None),
    references: UploadFile = File(None),
    artist_id: str = Form(..., min_length=40, max_length=40),
    estimated_budget: float = Form(),
    tattoo_placement: str = Form(..., max_length=20),
    is_first_time: bool = Form(default=False),
    is_work_in_progress: bool = Form(default=False),
):
    try:
        return JSONResponse(
            content={"detail": "Record created successfully."},
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
