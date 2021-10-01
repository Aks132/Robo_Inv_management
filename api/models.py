from django.db import models

# Create your models here.

class Electronics(models.Model):
    id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=20)
    taken_by = models.IntegerField()
    status = models.CharField(max_length=20)
    category = models.CharField(max_length=8)

    def __str__(self):
        return self.id

