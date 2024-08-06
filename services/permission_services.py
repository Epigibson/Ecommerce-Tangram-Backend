from uuid import UUID

from fastapi import HTTPException, status

from models.permission_model import Permission
from schemas.permission_schema import PermissionCreate, PermissionUpdate


class PermissionServices:

    @staticmethod
    async def create(data: PermissionCreate):
        try:
            result = Permission(**data.dict())
            await result.insert()
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e),
            )
        return {
            "message": "Permission created successfully",
            "result": result
        }

    @staticmethod
    async def retrieve(permission_id: UUID):
        try:
            result = await Permission.find_one(Permission.permission_id == permission_id)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e),
            )
        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Permission not found"
            )
        return {
            "message": "Permission retrieved successfully",
            "result": result
        }

    @staticmethod
    async def list():
        result = await Permission.find_all().to_list()
        return result

    @staticmethod
    async def update(permission_id: UUID, data: PermissionUpdate):
        result = await PermissionServices.retrieve(permission_id)
        await result.update({"$set": data.dict(exclude_unset=True)})
        await result.save()
        return result

    @staticmethod
    async def delete(permission_id: UUID):
        result = await PermissionServices.retrieve(permission_id)
        await result.delete()
        message = f"Permission {permission_id} deleted"
        return message
