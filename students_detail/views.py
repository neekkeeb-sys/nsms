from rest_framework import viewsets
from .models import StudentDetail
from .serializers import StudentDetailSerializer

class StudentDetailViewSet(viewsets.ModelViewSet):
    queryset = StudentDetail.objects.all()
    serializer_class = StudentDetailSerializer
