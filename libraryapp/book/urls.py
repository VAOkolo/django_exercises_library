from django.urls import path
from . import views

urlpatterns = [
    path('books/',views.home, name="books-name"),
    path('books/<int:id>',views.show, name="single-book")
]

