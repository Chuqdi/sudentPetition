
from django.urls import path
from .views import CreatePetitionView, DeletePetitionView, ListPetitionView, UpdatePetitionView



urlpatterns =[
    path("create/", CreatePetitionView.as_view(), name="create_petition"),
    path("update/<int:pk>/", UpdatePetitionView.as_view(), name="update_petition"),
    path("delete/<int:pk>/", DeletePetitionView.as_view(), name="delete_petition"),
    path("list/", ListPetitionView.as_view(), name="list_petition")
]