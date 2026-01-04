from django.urls import path
from .views import StudentViewSet


student_list = StudentViewSet.as_view({'get': 'list'})
nigita_list = StudentViewSet.as_view({'get': 'naresh'})
hari_list = StudentViewSet.as_view({'get': 'hari'})
sapana_list = StudentViewSet.as_view({'get': 'sapana'})
binita_list = StudentViewSet.as_view({'get': 'binita'})
nigita_list = StudentViewSet.as_view({'get': 'nigita'})

urlpatterns = [
    path('students/', student_list), 
    path('nigita/', nigita_list), 
    path('hari/', hari_list), 
    path('sapana/', sapana_list), 
    path('binita/', binita_list),
    path('nigita/', nigita_list),
]
