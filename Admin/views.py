from django.shortcuts import render,redirect
from Admin.models import *

# Create your views here.

def homepage(request):
    return render(request,"Admin/Homepage.html")

def adminreg(request):
    if request.method == "POST":
        tbl_admin.objects.create(admin_name=request.POST.get("txt_name"),admin_contact=request.POST.get("txt_contact"),admin_email=request.POST.get("txt_email"),admin_password=request.POST.get("txt_password"))
        return redirect("webadmin:adminreg")
    else:
        return render(request,"Admin/Admin_reg.html")

def addproject(request):
    typ = tbl_type.objects.all()
    pro = tbl_project.objects.all()
    if request.method == "POST":
        typ = tbl_type.objects.get(id=request.POST.get("sel_type"))
        tbl_project.objects.create(project_name=request.POST.get("txt_name"),project_description=request.POST.get("txt_desc"),project_status=request.POST.get("sel_status"),type_id=typ)
        return redirect("webadmin:addproject")
    else:
        return render(request,"Admin/Add_project.html",{"type":typ,"project":pro})

def deleteproject(request,id):
    tbl_project.objects.get(id=id).delete()
    return redirect("webadmin:addproject")

def projecttype(request):
    typ = tbl_type.objects.all()
    if request.method == "POST":
        tbl_type.objects.create(type_name=request.POST.get("txt_type"))
        return redirect("webadmin:projecttype")
    else:
        return render(request,"Admin/Add_type.html",{"type":typ})

def deletetype(request,id):
    tbl_type.objects.get(id=id).delete()
    return redirect("webadmin:projecttype")

def edittype(request,id):
    typ = tbl_type.objects.get(id=id)
    if request.method == "POST":
        typ.type_name = request.POST.get("txt_type")
        typ.save()
        return redirect("webadmin:projecttype")
    else:
        return render(request,"Admin/Add_type.html",{"typ":typ})


def adduser(request):
    user = tbl_user.objects.all()
    if request.method == "POST":
        tbl_user.objects.create(first_name=request.POST.get("txt_fname"),last_name=request.POST.get("txt_lname"),email=request.POST.get("txt_email"),password=request.POST.get("txt_password"),status=request.POST.get("sel_status"),role=request.POST.get("txt_role"))
        return redirect("webadmin:adduser")
    else:
        return render(request,"Admin/Add_user.html",{"user":user})

def delete_user(request,id):
    tbl_user.objects.get(id=id).delete()
    return redirect("webadmin:adduser")