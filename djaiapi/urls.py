from django.urls import path
from djaiapi import views

"""
urlpatterns = [
    path('hello/', views.hello_world),
]
"""

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]
