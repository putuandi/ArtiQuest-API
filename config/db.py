from sqlalchemy import create_engine, MetaData
# from sqlalchemy.orm import sessionmaker

engine=create_engine('')

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# con = SessionLocal()

meta=MetaData()
con=engine.connect()
