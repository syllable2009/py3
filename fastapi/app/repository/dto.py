from pydantic import BaseModel

class BaseDTO(BaseModel):
    id: int

class UserDTO(BaseDTO):
    name: str
    fullname: str
    desc: str
