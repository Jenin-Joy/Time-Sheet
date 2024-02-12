from django.urls import path
from Admin import views
app_name = "webadmin"
urlpatterns = [
    path("homepage/",views.homepage,name="homepage"),
    path("addproject/",views.addproject,name="addproject"),
    path("deleteproject/<int:id>",views.deleteproject,name="deleteproject"),
    path("adduser/",views.adduser,name="adduser"),
    path("adminreg/",views.adminreg,name="adminreg"),
    path("projecttype/",views.projecttype,name="projecttype"),
    path("deletetype/<int:id>",views.deletetype,name="deletetype"),
    path("edittype/<int:id>",views.edittype,name="edittype"),
    path("delete_user/<int:id>",views.delete_user,name="delete_user"),
]