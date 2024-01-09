from django.db import models

class Phone(models.Model):
    brand=models.CharField(max_length=100)
    model=models.CharField(max_length=100)
    storage=models.CharField(max_length=100)
    ram=models.CharField(max_length=100)
    frontCamera=models.CharField(max_length=100)
    backCamera=models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    price=models.IntegerField()
    os=models.CharField(max_length=100)
    isActive=models.BooleanField(default=True)
    image = models.ImageField(upload_to='phone_images/', null=True, blank=True)

    def __str__(self):
        return self.brand+" "+self.model














