
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import date

students = []
attendance = []
student_id = 1


@api_view(['POST'])
def add_student(request):
    global student_id
    student = {
        "id": student_id,
        "name": request.data.get("name"),
        "class": request.data.get("class"),
    }
    students.append(student)
    student_id += 1
    return Response(student)


@api_view(['GET'])
def all_students(request):
    return Response(students)


@api_view(['POST'])
def mark_attendance(request):
    record = {
        "student_id": request.data.get("student_id"),
        "status": request.data.get("status"),  # Present / Absent
        "date": str(date.today())
    }
    attendance.append(record)
    return Response(record)


@api_view(['GET'])
def today_attendance(request):
    today = str(date.today())
    today_records = [a for a in attendance if a["date"] == today]
    return Response(today_records)


@api_view(['DELETE'])
def remove_student(request, id):
    global students
    students = [s for s in students if s["id"] != id]
    return Response({"message": "Student removed successfully"})
