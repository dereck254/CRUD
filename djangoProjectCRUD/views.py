from django.shortcuts import render, redirect
from . models import Student
def displayindex(request):
    data = Student.objects.all()
    context = {"data" : data}
    return render(request, "index.html", context)

def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phonenum = request.POST.get('phonenum')

        query = Student(name=name, email=email, phonenum=phonenum)
        query.save()
        return redirect("/")
    return render(request, "index.html")

def deleteData(request, id):
    d = Student.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request, "index.html")

def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phonenum = request.POST.get('phonenum')

        edit = Student.objects.get(id = id)
        edit.name = name
        edit.email = email
        edit.phonenum = phonenum
        edit.save()
        return redirect("/")
    d = Student.objects.get(id=id)
    context = {"d" : d}
    return render(request, "edit.html", context)