from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from person.schemas import Person, Race
from person.models import races_table, person_table
from database import get_async_session

primarhs_db = [
    {"id": 1, "name": "Лев Эль’Джонсон", "race": 0, "role": "Примарх", "world": "Калибан", "alive": True},
    {"id": 3, "name": "Фулгрим", "race": 0, "role": "Примарх", "world": "Кемос", "alive": True},
    {"id": 4, "name": "Пертурабо", "race": 0, "role": "Примарх", "world": "Олимпия", "alive": True},
    {"id": 5, "name": "Джагатай Хан", "race": 0, "role": "Примарх", "world": "Чогорис", "alive": True},
    {"id": 6, "name": "Леман Русс", "race": 0, "role": "Примарх", "world": "Фенрис", "alive": True},
    {"id": 7, "name": "Рогал Дорн", "race": 0, "role": "Примарх", "world": "Инвит", "alive": True},
    {"id": 8, "name": "Конрад Кёрз", "race": 0, "role": "Примарх", "world": "Нострамо", "alive": True},
    {"id": 9, "name": "Сангвиний", "race": 0, "role": "Примарх", "world": "Ваал", "alive": True},
    {"id": 10, "name": "Феррус Манус", "race": 0, "role": "Примарх", "world": "Медуза", "alive": True},
    {"id": 12, "name": "Ангрон", "race": 0, "role": "Примарх", "world": "Нуреция", "alive": True},
    {"id": 13, "name": "Робаут Жиллиман", "race": 0, "role": "Примарх", "world": "Макрагг", "alive": True},
    {"id": 14, "name": "Мортарион", "race": 0, "role": "Примарх", "world": "Барбарус", "alive": True},
    {"id": 15, "name": "Магнус Красный", "race": 0, "role": "Примарх", "world": "Просперо", "alive": True},
    {"id": 16, "name": "Хорус Луперкаль", "race": 0, "role": "Примарх", "world": "Хтония", "alive": True},
    {"id": 17, "name": "Лоргар Аврелиан", "race": 0, "role": "Примарх", "world": "Колхида", "alive": True},
    {"id": 18, "name": "Вулкан", "race": 0, "role": "Примарх", "world": "Ноктюрн", "alive": True},
    {"id": 19, "name": "Корвус Коракс", "race": 0, "role": "Примарх", "world": "Коракс", "alive": True},
    {"id": 20, "name": "Альфарий/Омегон", "race": 0, "role": "Примарх", "world": "Терра", "alive": True},
]

router = APIRouter(
    prefix="/person",
    tags=['Person']
)

@router.get("/race/{race_id}/", response_model=List[Race])
async def get_one_race(race_id: int, session: AsyncSession = Depends(get_async_session)):
    """This method get data about one race from DB"""
    query = select(races_table).where(races_table.c.id == race_id)
    result = await session.execute(query)
    return result.all()


@router.post("/race/")
async def add_race(race_data: Race, session: AsyncSession = Depends(get_async_session)):
    """
    This method add new race in DB
    :arg: race_data - data in request body about one race
    """
    stmt = insert(races_table).values(**race_data.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.get("/{person_id}/", response_model=List[Person])
async def get_person(person_id: int, session: AsyncSession = Depends(get_async_session)):
    """This method get data about one person from DB"""
    query = select(person_table).where(person_table.c.id == person_id)
    result = await session.execute(query)
    return result.all()


@router.post("/")
async def add_person(person_data: Person, session: AsyncSession = Depends(get_async_session)):
    """
    This method add new person in DB
    :arg: person_data - data in request body about one person
    """
    stmt = insert(person_table).values(**person_data.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}



