from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status

class StudentViewSet(ViewSet):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    def store(self, request):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Student created successfully",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
        
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
    def destroy(self, request):
    student_id = request.data.get('id')

    # 1️⃣ Check id is provided
    if not student_id:
        return Response(
            {"error": "Student id is required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    # 2️⃣ Get student object
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return Response(
            {"error": "Student not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    # 3️⃣ Delete student
    student.delete()

    return Response(
        {
            "message": "Student deleted successfully",
            "deleted_id": student_id
        },
        status=status.HTTP_204_NO_CONTENT
    )
