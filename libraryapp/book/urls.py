from django.urls import path
from . import views

urlpatterns = [
    path('',views.base, name="base"),
    path('books/',views.home, name="books-name"),
    path('books/<int:id>',views.show, name="single-book")
]
