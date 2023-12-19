from sqlalchemy import create_engine, MetaData
# engine=create_engine('mysql+mysqlconnector://root@localhost:3306/artiquest_database')
engine=create_engine('mysql+mysqlconnector://root:12345678@34.101.61.129:3306/artiquest_database')
meta=MetaData()
con=engine.connect()