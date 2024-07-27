from typing import Literal

from pydantic import BaseModel

class PaymentConfirmationIn(BaseModel):
    """Represents the incoming data for a payment confirmation."""

    status: Literal["approved", "rejected", "failed"]  # see the PaymentStatus enum in the domain


__all__ = ["PaymentConfirmationIn"]
