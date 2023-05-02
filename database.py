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

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(row._asdict())

        return jobs