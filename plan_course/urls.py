from django.urls import pathlib
from .views import plan_course

urlpatterns = [
    path('plan-course/', plan_course, name='plan-course'),
]