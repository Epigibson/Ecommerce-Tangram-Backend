from typing import Optional
from uuid import UUID

import mercadopago
from beanie import PydanticObjectId

from core.config import settings
from models.user_model import User


class MercadoPagoService:

    @staticmethod
    async def create_preference(user_id: UUID, products: Optional[list[PydanticObjectId]] = None):
        # user = await User.find_one(User.user_id == user_id)
        # sdk = mercadopago.SDK(settings.MERCADO_PAGO_ACCESS_TOKEN)
        # items = []
        # for element in products:
        #     product = await ProductService.get_product_by_object_id(element)
        #
        #     category = await Category.find_one(Category.id == product.category)
        #     items.append(
        #         {
        #             "id": product.brand,
        #             "title": product.product_name,
        #             "quantity": 1,
        #             "unit_price": product.price,
        #             "currency_id": "MEX",
        #             "picture_url": product.images[0] if product.images else '',
        #             "description": product.product_description,
        #             "category_id": category.name if category else None,
        #         }
        #     )
        #
        # auto_return = "approved"
        #
        # back_urls = {
        #     "failure": "https://ais-sport-manage-frontend.vercel.app/pago/fallo",
        #     "pending": "https://ais-sport-manage-frontend.vercel.app/pago/pendiente",
        #     "success": "https://ais-sport-manage-frontend.vercel.app/pago/exito"
        # }
        #
        # payer = {
        #     "name": user.name,
        #     "surname": user.username,
        #     "email": user.email,
        #     "phone": {
        #         "area_code": "52",
        #         "number": user.mobile
        #     },
        #     "address": {
        #         "street_name": user.street_name,
        #         "street_number": user.street_number,
        #         "zip_code": user.zip_code,
        #     }
        # }
        #
        # preference_data = {"items": items, "auto_return": auto_return, "back_urls": back_urls, "payer": payer}
        # preference_response = sdk.preference().create(preference_data)
        # preference = preference_response["response"]
        # return preference
        pass
