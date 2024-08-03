from pydantic import BaseModel


class PaymentData(BaseModel):
    """
    Create Payment Data Schema
    """
    action: str
    api_version: str
    data: dict
    date_created: str
    id: int
    live_mode: bool
    type: str
    user_id: int