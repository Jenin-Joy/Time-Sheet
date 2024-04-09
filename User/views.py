from django.shortcuts import render,redirect
from Admin.models import tbl_user,tbl_project
from User.models import *
from django.db.models import Sum
# Create your views here.

def homepage(request):
    if "uid" in request.session:
        user = tbl_user.objects.get(id=request.session["uid"])
        return render(request,"User/Homepage.html",{"user":user})
    else:
        return redirect("webguest:login")

def timesheet(request):
    if "uid" in request.session:
        project = tbl_project.objects.all()
        hours = tbl_hours.objects.filter(user=request.session["uid"])
        count = range(1 , 8)
        return render(request,"User/TimeSheet.html",{"prj":project,"hours":hours,"count":count})
    else:
        return redirect("webguest:login")

def ajaxinsert(request):
    project = tbl_project.objects.get(id=request.GET.get("projectid"))
    user = tbl_user.objects.get(id=request.session["uid"])
    tbl_hours.objects.create(project=project,user=user,work_date=request.GET.get('day'),hour=request.GET.get("hour"),)
    return render(request,"User/AjaxInsert.html")

def ajaxchecker(request):
    if (request.GET.get("date") != "") and (request.GET.get("projectid") != ""):
        data = tbl_hours.objects.filter(work_date=request.GET.get("date"),project=request.GET.get("projectid"))
        return render(request,"User/AjaxChecker.html",{"data":data})
    else:
        return render(request,"User/AjaxChecker.html")

def logout(request):
    del request.session["uid"]
    return redirect("webguest:login")