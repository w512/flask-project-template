import os
import datetime
import redis

from sqlalchemy import (
    Integer,
    String,
    Text,
    Boolean,
    DateTime,
    Column,
    ForeignKey,
    create_engine,
)
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base

from source.local_settings import (
    DB_ENGINE,
    REDIS_HOST,
    REDIS_PORT,
    REDIS_DB_NUMBER,
)


Redis_DB = redis.StrictRedis(
    host=REDIS_HOST, 
    port=REDIS_PORT, 
    db=REDIS_DB_NUMBER
)

Base = declarative_base()
engine = create_engine(DB_ENGINE)
DBSession = sessionmaker(bind=engine)


# The examples of Models ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(Integer, nullable=False)
    
    comments = relationship(
        'Comment',
        back_populates='user',
        cascade='all, delete, delete-orphan'
    )


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    text = Column(String(300), nullable=False)
    tags = Column(ARRAY(String(80)), default=[])
    date = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship(
        'User',
        back_populates='comments',
    )

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Base.metadata.create_all(engine)

