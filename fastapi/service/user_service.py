from models.user import User
from utils.logger import logger
from typing import List


users_db = []

async def create_user(users: List[User]):
    created_users = []

    for user in users:
        if any(existing_user.id == user.id for existing_user in users_db):
            logger.warning(f"User with ID '{user.id}' already exists.")
            continue 

        logger.info(f"Creating user: {user.name}")
        users_db.append(user)
        created_users.append({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "department": user.department,
            "location": user.location
        })

    if not created_users:
        return {"message": "No new users were created"}

    return {"message": "Users created", "users": created_users}


def search_by_location(location: str):
    return [
        user for user in users_db
        if location.lower() in user.location.lower()
    ]


def search_by_department(department: str):
    return [
        user for user in users_db
        if department.lower() in user.department.lower()
    ]


def search_by_id(user_id: str):
    for user in users_db:
        if user.id == user_id:
            return user
    return None


def search_by_name(name: str):
    return [
        user for user in users_db
        if name.lower() in user.name.lower()
    ]