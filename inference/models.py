from django.db import models

# Create your models here.
class File(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return str(self.id)
