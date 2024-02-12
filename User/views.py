from django.shortcuts import render,redirect
from Admin.models import tbl_user,tbl_project
from User.models import *
from django.db.models import Sum
# Create your views here.

def homepage(request):
    user = tbl_user.objects.get(id=request.session["uid"])
    return render(request,"User/Homepage.html",{"user":user})

def timesheet(request):
    # hr = tbl_hours.objects.filter(user=request.session["uid"])
    # totals = hr.aggregate(
    # total_monday=Sum('monday'),
    # total_tuesday=Sum('tuesday'),
    # total_wednesday=Sum('wednesday'),
    # total_thursday=Sum('thursday'),
    # total_friday=Sum('friday'),
    # total_saturday=Sum('saturday'),
    # total_sunday=Sum('sunday')
    # )
    # if request.method == "POST":
    #     prj = tbl_project.objects.get(id=request.POST.get("sel_project"))
    #     user = tbl_user.objects.get(id=request.session["uid"])
    #     tbl_hours.objects.create(project=prj,user=user,monday=request.POST.get("txt_mon"),tuesday=request.POST.get("txt_tue"),wednesday=request.POST.get("txt_wed"),thursday=request.POST.get("txt_thu"),friday=request.POST.get("txt_fri"),saturday=request.POST.get("txt_sat"),sunday=request.POST.get("txt_sun"))
    #     return redirect("webuser:timesheet")
    # else:
    project = tbl_project.objects.all()
    hours = tbl_hours.objects.filter(user=request.session["uid"])
    count = range(1 , 8)
    return render(request,"User/TimeSheet.html",{"prj":project,"hours":hours,"count":count})

def ajaxinsert(request):
    project = tbl_project.objects.get(id=request.GET.get("projectid"))
    user = tbl_user.objects.get(id=request.session["uid"])
    tbl_hours.objects.create(project=project,user=user,work_date=request.GET.get('day'),hour=request.GET.get("hour"),)
    return render(request,"User/AjaxInsert.html")

def ajaxchecker(request):
    if (request.GET.get("date") != "") and (request.GET.get("projectid") != ""):
        data = tbl_hours.objects.get(work_date=request.GET.get("date"),project=request.GET.get("projectid"))
        return render(request,"User/AjaxChecker.html",{"data":data})
    else:
        return render(request,"User/AjaxChecker.html")