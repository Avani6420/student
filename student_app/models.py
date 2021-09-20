from django.db import models


class student(models.Model):
    Name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15, default=True)
    img = models.ImageField(upload_to='pics')
    email = models.CharField(max_length=50)
    city = models.CharField(max_length=100)

    class Meta:
        db_table = 'student'

# Create your models here.
