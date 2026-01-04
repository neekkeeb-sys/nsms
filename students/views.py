from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(ViewSet):
    def list(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    def naresh(self, request):
        return Response({"message": "Hello, Naresh!"})
    
    def hari(self, request):
        return Response({"message": "Hello, Hari!"})

    def sapana(self, request):
        return Response({"message": "Hello sapana!"})


    def binita(self, request):
        return Response({"message": "Hello binita!"})

    def nigita(self, request):
        return Response({"message": "myname is nigita! i am from nepal"})

    def naresh(self, request):
        return Response({"message": "neresh is a good preson! he very curious person i love naresh"})