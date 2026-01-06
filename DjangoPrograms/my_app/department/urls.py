from django.urls import path
from . import views
urlpatterns = [
    path('', views.department_home, name='department_home'),
]
