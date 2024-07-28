from typing import Literal
from uuid import UUID

from pydantic import BaseModel

from src.core.domain.entities.payment import PaymentStatus


class PaymentConfirmationIn(BaseModel):
    """Represents the incoming data for a payment confirmation."""

    status: Literal["approved", "rejected", "failed"]  # see the PaymentStatus enum in the domain


class PaymentSummaryOut(BaseModel):
    """Represents the outgoing data for a payment confirmation."""

    status: PaymentStatus
    number: UUID


__all__ = ["PaymentConfirmationIn", "PaymentSummaryOut"]
