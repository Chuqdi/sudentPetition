

from django.urls import path
from .views import editProfile

urlpatterns =[
    path("edit_profile/", editProfile, name="edit_profile")
]