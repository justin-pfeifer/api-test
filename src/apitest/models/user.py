from datetime import date
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    joined: date

    @classmethod
    def resolve(cls, id: int):
        return cls(id=id, name='test', joined=date.today())