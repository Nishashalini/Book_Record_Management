from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Employee
def employee_info_view(request):
    employees=Employee.objects.all()
    data={'employees':employees}
    res=render(request,'testapp/employees.html',data)
    return(res)
def greeting(request):
    s="<h1>Hello and welcome to first view of testapp<h1><p>this is landing pagr</p>"
    return HttpResponse(s)
def showcontact(request):
    s="<h1>Contact page</h1>"
    s+="<p>Websites: mysirg.com</p>"
    s+="<p>Mobile no: 7392938459"
    s+="<p>Email: priyamshalini999@gmail.com</p>"
    return HttpResponse(s)
def about(request):
    text="This is an about page"
    return render(request, 'testapp/about.html',{'text':text})
