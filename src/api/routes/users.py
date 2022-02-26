from typing import Optional, List
from models.user import User
from fastapi import APIRouter, status
from datetime import date
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

users = APIRouter(prefix='/users', tags=['Users'])

@users.get('/', response_model=List[User], 
tags=['Users'], 
summary='test',
responses={
    201: {'description': 'this is a test', 
    'content': {
        'application/json': {
            'example': User.resolve(0)
        },
        'test/taco': {
            'example': 'fred'
        }
    }
    }
})
def get_user_list() -> List[User]:
    """
        # Test
        * 1
        * 2
    """
    user = [User(id=2, name='test', joined=date.today())]
    return JSONResponse(content=jsonable_encoder(user), status_code=200)

@users.get('/{id}', response_model=User, tags=['Users'])
def get_user(id: int=2) -> User:
    """TEsting"""
    user = User.resolve(id=id)
    return user