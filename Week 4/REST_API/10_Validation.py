from pydantic import BaseModel,Field

class Student(BaseModel):

    name:str

    age:int=Field(

        gt=18,

        lt=60

    )