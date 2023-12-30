from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Package(BaseModel):
    """
    class
    """
    name: str
    number: str
    description: Optional[str] = None

app = FastAPI()

@app.get('/')
async def hello_world():
    """
    Hello world app
    uvicorn in subdirectory: uvicorn dir.subdir.file:method
    """
    return {"Hello": "World"}

@app.post("/package/{priority}")
async def make_package(priority: int, package: Package, value: bool):
    """
    BaseModel
    """
    return {"priority": priority, **package.model_dump(), "value": value} 
    # .dict() is depreciated, use model_dump()

# @app.get("/component/{component_id}") #path parameter
# async def get_component(component_id: int):
#     """
#     component id
#     """
#     return {"component_id": component_id}

# @app.get("/component/") #query parameter
# async def read_component(number: int, text: Optional[str]):
#     """
#     query parameters
#     """
#     return {"number": number, "text": text}

