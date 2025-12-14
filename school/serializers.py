from rest_framework import serializers
from .models import Program , Event , Teacher , Grade , Review,Testimonial,Student




class TeatcherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"



