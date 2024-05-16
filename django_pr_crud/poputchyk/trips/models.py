from django.db import models



class Trip(models.Model):
    
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    start = models.CharField(max_length=20)
    finish = models.CharField(max_length=20)
    date = models.DateField()


    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering = ['date']

