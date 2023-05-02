from sqlalchemy import create_engine, text
import os

username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')
host = os.environ.get('HOST')
database = os.environ.get('DATABASE')



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