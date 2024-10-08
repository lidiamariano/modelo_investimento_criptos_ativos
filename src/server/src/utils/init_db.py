from src.models.settings.base import Base
from src.models.settings.connection import engine
from src.models.entities.bitcoin import Bitcoin
from src.models.entities.ethereum import Ethereum
from src.models.entities.predict import Predict

def create_tables():
  Base.metadata.create_all(bind=engine)
  Bitcoin.metadata.create_all(bind=engine)
  Ethereum.metadata.create_all(bind=engine)
  Predict.metadata.create_all(bind=engine)