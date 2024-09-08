from django.shortcuts import render
from rest_framework import generics
from tcaapp.models import studentData
from tcaapp.serializers import studentDataSerializer

class studentApiCreate(generics.CreateAPIView):
    queryset=studentData
    serializer_class=studentDataSerializer

class studentApiUpdate(generics.UpdateAPIView):
    queryset=studentData
    serializer_class=studentDataSerializer
    lookup_field="name"

class studentApiDelete(generics.DestroyAPIView):
    queryset=studentData
    serializer_class=studentDataSerializer
    lookup_field="name"
    
class studentApiRetrieve(generics.RetrieveAPIView):
    queryset=studentData
    serializer_class=studentDataSerializer
    lookup_field="name"
