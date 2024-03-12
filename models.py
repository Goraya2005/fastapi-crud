
from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum




class Gender(str, Enum):
    male = "male"
    female = "female"


class Role(str, Enum):
    user = "user"
    admin = 'admin'
    student = "student"



class User(BaseModel):
    id : Optional[int]
    first_name : str
    last_name: str
    gender : Gender
    role : List[Role]
