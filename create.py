from connection import data
from models import Base

Base.metadata.create_all(bind=data)