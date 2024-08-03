from uuid import UUID
from cloudinary.uploader import upload
import core.cloudinary_config
from fastapi import UploadFile, File

from services.user_services import UserService


class ChangeUserAvatarService:

    @staticmethod
    async def change_avatar_for_user(user_id: UUID, file: UploadFile = File(...)):
        user = await UserService.get_user_by_id(user_id)
        result = upload(file.file.read(), folder="ticket_files/")
        user.avatar = result["secure_url"]
        await user.save()
        return user
