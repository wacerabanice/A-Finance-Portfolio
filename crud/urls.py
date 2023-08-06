from django.urls import path
from . import views

app_name = 'crud'

urlpatterns = [
    path('', views.home, name='home'),
    path('insertdata', views.insertdata, name="insertdata"),
    path('delete/<id>', views.delete, name="delete"),
    path('editdata/<id>', views.editdata, name="editdata")
]
