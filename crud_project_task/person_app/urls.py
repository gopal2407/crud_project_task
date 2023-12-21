from django.urls import path
from .views import create_person, show_persons, retrieve_person, update_person,  delete_person

urlpatterns = [
    path('create-person/', create_person),
    path('show-persons/', show_persons),
    path('retrieve-person/<int:pk>/', retrieve_person),
    path('update-person/<int:pk>/', update_person),
    path('delete-person/<int:pk>/', delete_person)
]