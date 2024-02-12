from django.shortcuts import render,redirect
from Admin.models import *
# Create your views here.

def login(request):
    if request.method == "POST":
        admincount = tbl_admin.objects.filter(admin_email=request.POST.get("txt_email"),admin_password=request.POST.get("txt_password")).count()
        usercount = tbl_user.objects.filter(email=request.POST.get("txt_email"),password=request.POST.get("txt_password")).count()
        if admincount > 0:
            admin = tbl_admin.objects.get(admin_email=request.POST.get("txt_email"),admin_password=request.POST.get("txt_password"))
            request.session["aid"] = admin.id
            return redirect("webadmin:homepage")
        elif usercount > 0:
            user = tbl_user.objects.get(email=request.POST.get("txt_email"),password=request.POST.get("txt_password"))
            request.session["uid"] = user.id
            return redirect("webuser:homepage")
        else:
            return render(request,"Guest/Login.html",{"msg":"Error in email or password...!!"})
    else:
        return render(request,"Guest/Login.html")