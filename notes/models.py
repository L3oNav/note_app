from django.db import models
from utils import BaseModel

# Create your models here.

class NoteModel(BaseModel):

    user = models.EmailField()

    title = models.CharField(max_length=255)

    content = models.TextField()

    is_public = models.BooleanField(default=False)


    def __str__(self):
        return self.title
