from django.db import models

class family(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    BirthDate = models.DateField()

    def __str__(self):
        return f"{self.name} {self.last_name}"
