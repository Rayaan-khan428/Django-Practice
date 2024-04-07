from django.db import models

# Create your models here.

# Model to define how the Todo items should be stored in the database
# describing the three properties of the todo model
class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title
    
