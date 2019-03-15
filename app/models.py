from django.db import models

# Create your models here.
class Wheel(models.Model):
    bg = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    class Meta:
        db_table = 'mml_wheel'
