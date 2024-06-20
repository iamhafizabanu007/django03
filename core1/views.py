from django.shortcuts import redirect, render
from django.views import View
from .models import Students
from .forms import AddStudentForm
# Create your views here.

class Home(View):
    def get(self,request):
        student_data=Students.objects.all()
        return render(request,'core1/home.html',{'stu_data':student_data})
class Add_Students(View):
    def get(self,request):
        fm=AddStudentForm()
        return render(request,'core1/add_student.html',{'form':fm})
    
    def post(self,request):
        fm=AddStudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request,'core1/add-student.html',{'form':fm})
class Deleting_student(View):
    def post(self, request):
        data=request.POST
        id=data.get('id')
        student=Students.objects.get(id=id)
        student.delete()
        return redirect('/')
    
class EditStudent(View):
    def get(self, request, id):
         stu=Students.objects.get(id=id)
         fm=AddStudentForm(instance=stu)
         return render(request,'core1/edit-student.html',{'form':fm})
    def post(self,request,id):
        stu=Students.objects.get(id=id)
        fm=AddStudentForm(request.POST,instance=stu)
        if fm.is_valid():
            fm.save()
            return redirect('/')