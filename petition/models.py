from django.db import models
from django.utils import timezone
from student_management_app.models import CustomUser
from django.urls import reverse



class Petitions(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 200)
    content = models.TextField()
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_on = models.DateField(default= timezone.now)


    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse("update_petition", kwargs={"pk":self.pk})