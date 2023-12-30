from typing import Optional, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(tittle="Todo API")

class Todo(BaseModel):
    """
    Todo: create, read, update, delete
    """
    name: str
    due_date: str
    description: Optional[str]

# class Package(BaseModel):
#     """
#     class
#     """
#     name: str
#     number: str
#     description: Optional[str] = None

# class PackageIn(BaseModel):
#     """
#     class
#     """
#     secret_id: int
#     name: str
#     number: str
#     description: Optional[str] = None


store_todo = []

@app.get('/')
async def hello_world():
    """
    Hello world app
    uvicorn in subdirectory: uvicorn dir.subdir.file:method
    """
    return {"Hello": "World"}



# @app.post('/todo/')
# async def create_todo(todo: Todo):
#     """
#     create todo list
#     """
#     store_todo.append(todo)
#     return todo

# @app.get('/todo/', response_model=List[Todo])
# async def get_all_todos():
#     """
#     get all todos
#     """
#     return store_todo

# @app.get('/todo/{id}')
# async def get_todo(id: int):
#     """
#     get 1 todo'
#     """
#     try:
#         return store_todo[id]
#     except Exception as e:
#         raise HTTPException(status_code=404, detail="Todo not found") from e

# @app.put('/todo/{id}')
# async def update_todo(id: int, todo: Todo):
#     """
#     get method
#     """
#     try:
#         store_todo[id] = todo
#         return store_todo[id]
#     except Exception as e:
#         raise HTTPException(status_code=404, detail="Todo not found") from e

# @app.delete('/todo/{id}')
# async def delete_todo(id: int):
#     """
#     delete todo
#     """
#     try:
#         # obj = store_todo[id]
#         store_todo.pop(id)
#         return f"Todo {id} deleted!"
#     except Exception as e:
#         raise HTTPException(status_code=404, detail="Todo not found") from e

# @app.post("/package2/", response_model=Package)
# async def make_package_2(package: PackageIn):
#     """
#     response model
#     """
#     return package

# @app.post("/package/{priority}")
# async def make_package(priority: int, package: Package, value: bool):
#     """
#     BaseModel
#     """
#     return {"priority": priority, **package.model_dump(), "value": value} 
#     # .dict() is depreciated, use model_dump()

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
