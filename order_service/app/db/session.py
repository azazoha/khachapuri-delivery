from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_file = 'order_service/data/dev.db'
db_url = f'sqlite:///{db_file}'


engine = create_engine(
    db_url,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()