from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from legion.schemas import Legion
from legion.models import legion_table
from database import get_async_session


router = APIRouter(
    prefix="/legion",
    tags=['Legion']
)


@router.get("/{legion_id}", response_model=List[Legion])
async def get_legion(legion_id: int, session: AsyncSession = Depends(get_async_session)):
    """This method get data about one legion from DB"""
    query = select(legion_table).where(legion_table.c.id == legion_id)
    result = await session.execute(query)
    return result.all()


@router.post("/")
async def add_legion(legion_data: Legion, session: AsyncSession = Depends(get_async_session)):
    """
    This method add new legion in DB
    :arg: legion_data - data in request body about one legion
    """
    stmt = insert(legion_table).values(**legion_data.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
