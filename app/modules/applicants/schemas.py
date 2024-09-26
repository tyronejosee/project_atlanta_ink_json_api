"""Schemas for Applicants App."""

import re
from typing import Optional
from enum import Enum

from pydantic import BaseModel, Field, EmailStr, validator


class StatusChoices(str, Enum):

    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


class Applicant(BaseModel):

    name: str = Field(max_length=100)
    email: str = EmailStr()
    phone: str = Field(max_length=15)
    cv: Optional[str] = None
    message: Optional[str] = None
    status: StatusChoices = StatusChoices.PENDING

    @validator("phone")
    def validate_phone(cls, value: str):
        # Validation for phone number with Atlanta format
        phone_regex = r"^\+1404\d{7}$"
        if not re.match(phone_regex, value):
            raise ValueError(
                "Invalid phone number, format example: +1404XXXXXXX.",
            )
        return value

    @validator("cv")
    def validate_cv(cls, value):
        # Validation for input files to be PDFs
        if value and not value.lower().endswith(".pdf"):
            raise ValueError("The CV must be a PDF file.")
        return value
