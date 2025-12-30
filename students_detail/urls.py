from django.urls import path
from .views import *

urlpatterns = [
    path('students/', all_students),
    path('students/add/', add_student),
    path('attendance/mark/', mark_attendance),
    path('attendance/today/', today_attendance),
    path('students/remove/<int:id>/', remove_student),
]
