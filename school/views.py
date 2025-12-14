from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets,permissions

from .serializers import (
    ProgramSerializer,EventSerializer,TeatcherSerializer,
    TestimonialSerializer,StudentSerializer,GradeSerializer,
    ReviewSerializer
) 

from .models import Program,Event,Teacher,Testimonial,Student,Grade,Review




# Create your views here.
def hello_world(request):
    return HttpResponse("hello hamed")



class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer



class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
