from pydantic import BaseModel

class Artifact(BaseModel):
    name:str
    description:str
    image:str