from sqlalchemy import Table, Column, Integer, String, Boolean, MetaData

metadata = MetaData()

person_table = Table(
    "person",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column('race', Integer, nullable=False),
    Column('role', String, nullable=False),
    Column('world', String, default='Неизвестно'),
    Column('alive', Boolean, default=False)
)
