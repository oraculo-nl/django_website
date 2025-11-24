from members.views import hello_view, details
from django.urls import path

urlpatterns = [
    path('members', hello_view, name='hello-view'),
    path('members/details/<int:id>', details, name='details'),
]