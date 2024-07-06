from rest_framework import serializers
from app.models import *

class StudentMS(serializers.ModelSerializer):
    class Meta:
        model=student
        fields='__all__'