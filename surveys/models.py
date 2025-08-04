from django.db import models

class StudentSurvey(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    telephone_number = models.CharField(max_length=20)
    email = models.EmailField()
    date_of_survey = models.DateField()
    liked_most = models.JSONField(null=True, blank=True)
    source_of_interest = models.CharField(max_length=100)
    likelihood = models.CharField(max_length=50)
    comments = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
