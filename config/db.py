""" from sqlalchemy import create_engine, MetaData
# engine=create_engine('mysql+mysqlconnector://root@localhost:3306/artiquest_database')
engine=create_engine('mysql+mysqlconnector://root:12345678@34.142.199.170:3306/artiquest_database')
meta=MetaData()
con=engine.connect() """

from sqlalchemy import create_engine, MetaData

db_params = {
    "host": "34.142.199.170",
    "user": "root",
    "password": "12345678",
    "database": "artiquest_database"
}

# Buat string koneksi dari parameter
db_url = f"mysql+mysqlconnector://{db_params['user']}:{db_params['password']}@{db_params['host']}:3306/{db_params['database']}"

# Buat objek engine
engine = create_engine(db_url)

# Buat objek metadata
meta = MetaData()

# Buat koneksi
con = engine.connect()