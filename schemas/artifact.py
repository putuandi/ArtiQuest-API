from pydantic import BaseModel

class Artifact(BaseModel):
    name:str
    description:str
    image1:str
    image2:str
    image3:str
    location:str
    lat:float
    lon:float