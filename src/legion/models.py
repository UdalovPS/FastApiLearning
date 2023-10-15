from sqlalchemy import Table, Column, Integer, String, Boolean, ForeignKey

from database import METADATA

legion_table = Table(
    'legion',
    METADATA,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("primarh_id", Integer, ForeignKey('person.id', ondelete="CASCADE")),
    Column("loyalty", Boolean, default=True)
)
