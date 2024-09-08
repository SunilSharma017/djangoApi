from rest_framework import serializers
from tcaapp.models import studentData

class studentDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=studentData
        fields=['name','email','percentage','grade']