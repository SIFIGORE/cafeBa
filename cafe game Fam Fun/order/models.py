from django.db import models
from jalali_date import datetime2jalali



class orders(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)
    #t = to_current_timezone(created)

    def __str__(self) -> str :
        return f'{self.id} - {self.name}'

    @property
    def get_jalali_date(self) :
        self.date = datetime2jalali(self.created)
        self.r = str(self.date)
        return self.r
    
