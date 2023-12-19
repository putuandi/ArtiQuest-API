from config.db import meta
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer,String


artifacts=Table(
    'artifacts',meta,
    Column('id',Integer,primary_key=True),
    Column('name',String(255)),
    Column('description',String(255)),
    Column('image',String(255)),
)