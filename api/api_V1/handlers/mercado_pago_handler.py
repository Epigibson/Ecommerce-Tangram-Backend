from uuid import UUID

from beanie import PydanticObjectId
from fastapi import APIRouter
from services.mercado_pago_checkout_service import MercadoPagoService

mercado_pago_router = APIRouter()


@mercado_pago_router.post("/mercado_pago/webhook", tags=["mercado pago"])
async def mercado_pago_webhook(products_list: list[PydanticObjectId], user: UUID):
    try:
        result = await MercadoPagoService.create_preference(user, products_list)
        return result
    except Exception as e:
        print(e)
        return {"message": "Error"}
