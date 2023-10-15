from fastapi import APIRouter
from typing import List

from legion.schemas import Legion



router = APIRouter(
    prefix="/legion",
    tags=['Legion']
)


legion_db = [
    {"id": 1, "name": "Темные ангелы", "primarh_id": 1, "loyalty": True}
]


@router.get("/{legion_id}")
async def get_legion(legion_id: int):
    """This method get data about one legion from DB"""
    return [legion for legion in legion_db if legion.get("id") == legion_id]


@router.post("/")
async def add_legion(legion_data: List[Legion]):
    """
    This method add new legion in DB
    :arg: legion_data - data in request body about one legion
    """
    legion_db.extend(legion_data)
    return legion_db
