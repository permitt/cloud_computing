from . import views
from django.urls import path, include

urlpatterns = [
    path('employee/', views.get_all),
    path('employee/<int:id>/', views.get_employee),
    path('count/', views.count)
]