from sqlalchemy import Table, Column, Integer, String, Boolean, ForeignKey

from database import METADATA

races_table = Table(
    'races',
    METADATA,
    Column("id", Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('home', String, nullable=False),
)

person_table = Table(
    "person",
    METADATA,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column('race', Integer, ForeignKey("races.id", ondelete="CASCADE")),
    Column('role', String, nullable=False),
    Column('world', String, default='Неизвестно'),
    Column('alive', Boolean, default=False)
)
