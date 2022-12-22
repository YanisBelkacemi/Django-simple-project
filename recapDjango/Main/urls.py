from django.urls import path
from . import views

urlpatterns = [
    path("", views.home , name= 'Home'),
    path('list/<int:id>', views.list , name='List'),
    path('create/', views.create, name='create'),
    path('delete/', views.delete, name='delete')
    
    

]