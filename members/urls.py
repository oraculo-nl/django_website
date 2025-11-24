from members.views import hello_view, details, main
from django.urls import path

urlpatterns = [
    path('', main, name='main'),
    path('members/', hello_view, name='hello-view'),
    path('members/details/<int:id>', details, name='details'),
]
