from pydantic import BaseModel


class Legion(BaseModel):
    """Validation class for legions in Warhammer 40k"""
    id: int
    name: str
    primarh_id: str
    loyalty: bool
