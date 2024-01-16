from typing import Optional, List
from fastapi import FastAPI, HTTPException, Form
from pydantic import BaseModel
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise
from Python.FastAPI.models import Todo, Todo_Pydantic, TodoIn_Pydantic


DESCRIPTION = """
## FastAPI Tutorial 
by [IsaiahTTech, 2021](https://www.youtube.com/@isaiahttech9749)

1. Getting Started
1. Path and Query
1. Pydantic BaseModel
1. Response Model
1. Simple Todo API
1. Forms
1. Tortoise ORM
1. Tortoise ORM with FastAPI Integration

"""
app = FastAPI(title="Todo API",
              description = DESCRIPTION,
              contact={
                  "name": "YouTube Playlist",
                  "url": "https://www.youtube.com/playlist?list=PLShTCj6cbon9gK9AbDSxZbas1F6b6C_Mx"
              },
              version="12/30/2023")

register_tortoise(
    app,
    db_url="sqlite:/store.db",
    modules={'models':['Python.FastAPI.models']},# notice path
    generate_schemas=True,
    add_exception_handlers=True
)

# class Todo(BaseModel):
#     """
#     Todo: create, read, update, delete
#     """
#     name: str
#     due_date: str
#     description: Optional[str]

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
async def home_page():
    """
    Home page
    uvicorn in subdirectory: uvicorn dir.subdir.file:method
    uvicorn Python.FastAPI.main:app --reload
    """
    return {"Hello": "World"}

@app.post('/todo/', response_model=Todo_Pydantic)
async def create(todo: TodoIn_Pydantic):
    """
    Pydantic todo
    """
    obj = await Todo.create(**todo.dict(exclude_unset=True))
    return await Todo_Pydantic.from_tortoise_orm(obj)

@app.get('/todo/{id}', response_model=Todo_Pydantic, responses={404: {"model": HTTPNotFoundError} })
async def get_one(app_id: int):
    """
    Get one query
    """
    return await Todo_Pydantic.from_queryset_single(Todo.get(todo_id=app_id))

# @app.post('/language/')
# async def language(name: str = Form(...), lang_type: str = Form(...)):
#     """
#     form, alternative to JSON
#     """
#     return {"name": name, "type": lang_type}


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

# @app.get('/todo/{my_id}')
# async def get_todo(my_id: int):
#     """
#     get 1 todo'
#     """
#     try:
#         return store_todo[my_id]
#     except Exception as e:
#         raise HTTPException(status_code=404, detail="Todo not found") from e

# @app.put('/todo/{my_id}')
# async def update_todo(my_id: int, todo: Todo):
#     """
#     get method
#     """
#     try:
#         store_todo[my_id] = todo
#         return store_todo[my_id]
#     except Exception as e:
#         raise HTTPException(status_code=404, detail="Todo not found") from e

# @app.delete('/todo/{my_id}')
# async def delete_todo(my_id: int):
#     """
#     delete todo
#     """
#     try:
#         # obj = store_todo[my_id]
#         store_todo.pop(my_id)
#         return f"Todo {my_id} deleted!"
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
#     component_id
#     """
#     return {"component_id": component_id}

# @app.get("/component/") #query parameter
# async def read_component(number: int, text: Optional[str]):
#     """
#     query parameters
#     """
#     return {"number": number, "text": text}
