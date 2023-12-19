from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table, select
from sqlalchemy.orm import declarative_base, Session, sessionmaker
from databases import Database

# Konfigurasi database
# DATABASE_URL = "mysql+mysqlconnector://root:12345678@34.101.61.129:80/artiquest_database"
DATABASE_URL = "mysql+mysqlconnector://root:@127.0.0.1:3306/artiquest_database"
engine = create_engine(DATABASE_URL)
database = Database(DATABASE_URL)
metadata = MetaData()

# Creating a SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Definisi model
Base = declarative_base()

class Gambar(Base):
    __table__ = Table(
        "db_gambar",
        metadata,
        Column("id_gambar", Integer, primary_key=True, index=True),
        Column("detail_gambar", String),
        Column("link_gambar", String),
    )

app = FastAPI()

def get_db():
    db = SessionLocal()  # Assuming SessionLocal is your SQLAlchemy database session
    try:
        yield db
    finally:
        db.close()

# Fungsi untuk mendapatkan detail gambar dan gambar dari database
@app.get("/gambar/{gambar_id}")
async def get_gambar(gambar_id: int, db: Session = Depends(get_db)):
    query = select(Gambar.__table__).where(Gambar.__table__.c.id_gambar == gambar_id)
    result = await database.fetch_one(query)
    if result is None:
        raise HTTPException(status_code=404, detail="Gambar not found")
    return result

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
