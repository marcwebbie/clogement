from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Course
from .serializers import CourseSerializer


@api_view(['GET'])
def courses(request):
    queryset = Course.objects.all()
    serializer = CourseSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def course_detail(request, slug):
    course = get_object_or_404(Course, api_slug=slug)
    serializer = CourseSerializer(course)
    return Response(serializer.data)
