from django.db import models


FEMALE = 1
MALE = 2
GENDER = (
    (FEMALE, 'FEMALE'),
    (MALE, 'MALE'),
)

class PhoneNumber(models.Model):
    class Meta:
        verbose_name = 'Телефонный Справочник'
        verbose_name_plural = 'Телефонный Справочник'
    number = models.CharField(max_length=50)
    name = models.CharField(max_length=150)
    city = models.CharField(max_length=150, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.IntegerField(choices=GENDER, null=True, blank=True)
    email = models.EmailField('email', null=True, max_length=100, blank=True)
    job_entry_time = models.DateTimeField(null=True, blank=True)
    job_quit_time = models.DateTimeField(null=True, blank=True)
    job_experience_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.number