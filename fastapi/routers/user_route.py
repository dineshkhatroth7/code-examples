from fastapi import APIRouter, HTTPException
from models.user import User
from service.user_service import (
    create_user,
    search_by_location,
    search_by_department,
    search_by_id,
    search_by_name
)
from typing import List

router = APIRouter()

@router.post("/")
async def add_users(users: List[User]):
    try:
        return await create_user(users)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/search/location")
async def search_users_by_location(location: str):
    try:
        results = search_by_location(location)
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/search/department")
async def search_users_by_department(department: str):
    try:
        results = search_by_department(department)
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/search/id")
async def search_user_by_id(user_id: int):
    try:
        user = search_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user.dict()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/search/name")
async def search_users_by_name(name: str):
    try:
        results = search_by_name(name)
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
