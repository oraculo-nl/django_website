from members.views import hello_view
from django.urls import path

urlpatterns = [
    path('members', hello_view, name='hello-view'),
]