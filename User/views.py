from django.shortcuts import render,redirect
from Admin.models import tbl_user,tbl_project
from User.models import *
from django.db.models import Sum
import datetime
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
        # Get the current year and week number
        current_date = datetime.datetime.now()
        current_year = current_date.year
        current_week = current_date.strftime("%W")

        # Initialize a list to store week options
        weeks = []

        # Generate week options for the dropdown
        for week_number in range(1, 53):
            # Get the start and end date of the week
            start_date = datetime.datetime.strptime(f'{current_year}-W{week_number}-1', "%Y-W%W-%w")
            end_date = start_date + datetime.timedelta(days=6)

            # Format the week option
            week_option = f"Week {str(week_number).zfill(2)} ({start_date.strftime('%b. %d, %Y')} - {end_date.strftime('%b. %d, %Y')})"
            weeks.append((f"{current_year}-W{str(week_number).zfill(2)}", week_option))

        # Pass weeks and current_week to the template context
        context = {
            'weeks': weeks,
            'current_week': f"{current_year}-W{current_week.zfill(2)}",
            # Other context variables...
        }
    
        return render(request,"User/TimeSheet.html",{"prj":project,"hours":hours,"count":count,'weeks': weeks})
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