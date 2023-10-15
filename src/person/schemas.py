from pydantic import BaseModel


class Race(BaseModel):
    """Validation class for Race in Warhammer 40k"""
    id: int
    name: str
    home: str


class Person(BaseModel):
    """Validation class for Person in Warhammer 40k"""
    id: int
    name: str
    race: int
    role: str
    world: str
    alive: bool
