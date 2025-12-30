
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# In-memory data (NO database)
students_data = []
counter = 1


@api_view(['GET'])
def get_students(request):
    return Response(students_data)


@api_view(['POST'])
def create_student(request):
    global counter
    student = {
        "id": counter,
        "name": request.data.get("name"),
        "class": request.data.get("class"),
        "age": request.data.get("age"),
    }
    students_data.append(student)
    counter += 1
    return Response(student, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def update_student(request, id):
    for student in students_data:
        if student["id"] == id:
            student["name"] = request.data.get("name", student["name"])
            student["class"] = request.data.get("class", student["class"])
            student["age"] = request.data.get("age", student["age"])
            return Response(student)
    return Response({"error": "Student not found"}, status=404)


@api_view(['DELETE'])
def delete_student(request, id):
    global students_data
    students_data = [s for s in students_data if s["id"] != id]
    return Response({"message": "Student deleted successfully"})
