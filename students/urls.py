from django.urls import path
from .views import *

urlpatterns = [
    path('students/', get_students),
    path('students/create/', create_student),
    path('students/update/<int:id>/', update_student),
    path('students/delete/<int:id>/', delete_student),
]
