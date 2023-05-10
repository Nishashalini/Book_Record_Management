from django.shortcuts import render
from django.http import HttpResponse

def showtest(request):
    que="Who developed C language"
    a="Ken Thompson"
    b="Dennis ritchie"
    c="Bjarne Stroustrup"
    d="Shalini"
    level="Easy"
    data={'que':que,'a':a,'b':b,'c':c,'d':d,'level':level}
    res=render(request,'exam/test.html',context=data)
    return res
def showresult(request):
    s="<h1>this is show result page</h1>"
    return HttpResponse(s)
