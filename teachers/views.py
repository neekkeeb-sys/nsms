
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# In-memory data (NO database)
teachers_data = []
counter = 1


@api_view(['GET'])
def get_teachers(request):
    return Response(teachers_data)


@api_view(['POST'])
def create_teacher(request):
    global counter
    teacher = {
        "id": counter,
        "name": request.data.get("name"),
        "subject": request.data.get("subject"),
    }
    teachers_data.append(teacher)
    counter += 1
    return Response(teacher, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def update_teacher(request, id):
    for teacher in teachers_data:
        if teacher["id"] == id:
            teacher["name"] = request.data.get("name", teacher["name"])
            teacher["subject"] = request.data.get("subject", teacher["subject"])
            return Response(teacher)
    return Response({"error": "Teacher not found"}, status=404)


@api_view(['DELETE'])
def delete_teacher(request, id):
    global teachers_data
    teachers_data = [t for t in teachers_data if t["id"] != id]
    return Response({"message": "Teacher deleted successfully"})
