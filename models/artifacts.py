from config.db import meta
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer,String,Text,Float


artifacts=Table(
    'artifacts',meta,
    Column('id',Integer,primary_key=True, autoincrement=True),
    Column('name',String(255)),
    Column('description',Text),
    Column('image1',String(255)),
    Column('image2',String(255)),
    Column('image3',String(255)),
    Column('location',String(255)),
    Column('lat',Float),
    Column('lon',Float),
)