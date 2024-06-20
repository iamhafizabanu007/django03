from django.urls import path
from .views import Home,Add_Students,Deleting_student,EditStudent
urlpatterns = [
    path('',Home.as_view(),name="home"),
    path('add-student/',Add_Students.as_view(),name="add-student"),
    path('del-student/',Deleting_student.as_view(),name="del-student"),
    path('editing/<int:id>/',EditStudent.as_view(),name="editing")
]