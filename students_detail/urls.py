# from django.urls import path
# from .views import *

# urlpatterns = [
#     path('students/', all_students),
#     path('students/add/', add_student),
#     path('attendance/mark/', mark_attendance),
#     path('attendance/today/', today_attendance),
#     path('students/remove/<int:id>/', remove_student),
# ]
# students_detail/urls.py
from django.urls import path
from .views import StudentListCreateAPIView, StudentRetrieveUpdateDestroyAPIView

urlpatterns = [
    # path('students/', StudentListCreateAPIView.as_view(), name='student-list'),
    # path('students/<int:pk>/', StudentRetrieveUpdateDestroyAPIView.as_view(), name='student-detail'),
]
