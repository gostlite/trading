from django.db import models
from pydantic import BaseModel , Field

# Create your models here.


class User(models.Model):
    first_name: str = Field()
    amount : int = Field()


class User1(BaseModel):
    # id: str = Field(default_factory=uuid.uuid4, alias="_id")    # _id = ObjectId(primary_key=True)
    first_name: str = Field()
    amount : int = Field()

    def __repr__(self):
        return f'{self.username} has been created'
