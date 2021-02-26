from django.db import models

# Create your models here.
class PhoneNumber(models.Model):
    class Meta:
        verbose_name = 'Телефонный Справочник'
        verbose_name_plural = 'Телефонный Справочник'
    number = models.CharField(max_length=50)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.number