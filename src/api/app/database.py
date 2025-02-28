from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://weatherapp_owner:npg_iugGnIe6W2By@ep-lively-credit-abilrk6a-pooler.eu-west-2.aws.neon.tech/weatherapp?sslmode=require"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()