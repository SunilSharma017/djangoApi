
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[
     path('',views.studentApiCreate.as_view(),name="studentApiCreate"),
     path('update/<str:name>',views.studentApiUpdate.as_view(),name="studentApiUpdate"),
     path('delete/<str:name>',views.studentApiDelete.as_view(),name="studentApiDelete"),
     path('view/<str:name>',views.studentApiRetrieve.as_view(),name="studentApiRetrieve"),

]