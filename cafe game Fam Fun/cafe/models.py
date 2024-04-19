from django.db import models

class food(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    category = models.ForeignKey("cafe.category", on_delete=models.CASCADE)
   
    def __str__(self) -> str :
        return f'{self.id} - {self.name}'

class category(models.Model):
    name = models.CharField(max_length=255)
   
    def __str__(self) -> str :
        return f'{self.id} - {self.name}'