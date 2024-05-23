from django.db import models

class game(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    
   
    def __str__(self) -> str :
        return f'{self.id} - {self.name}'

