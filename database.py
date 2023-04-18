from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
host = os.getenv('HOST')
database = os.getenv('DATABASE')



engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}/{database}?charset=utf8mb4",
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem",
        }
    }
    )

with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    result_dicts = []
    for row in result.all():
        result_dicts.append(row._asdict())

    print(result_dicts)
