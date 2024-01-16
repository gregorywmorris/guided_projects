from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator

class Todo(models.Model):
    """
    Todo class
    """
    todo_id = fields.IntField(pk=True)
    todo = fields.CharField(max_length=250)
    due_date = fields.CharField(max_length=250)
    
    class PydanticMeta:
        """
        Meta data
        """
        pass

Todo_Pydantic = pydantic_model_creator(Todo, name="Todo", exclude_readonly=True)
TodoIn_Pydantic = pydantic_model_creator(Todo, name="TodoIn", exclude_readonly=True)
