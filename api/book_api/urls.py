from django.urls import path
from . import views
urlpatterns = [
    path('', views.books), # localhost/books => GET, POST
    path('<int:id>', views.book_id), # localhost/books/1 => GET, PUT, DELETE
]
