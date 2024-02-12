from django.urls import path
from User import views
app_name = "webuser"
urlpatterns = [
    path("homepage/",views.homepage,name="homepage"),
    path('timesheet/',views.timesheet,name="timesheet"),
    path('ajaxinsert/',views.ajaxinsert,name="ajaxinsert"),
    path('ajaxchecker/',views.ajaxchecker,name="ajaxchecker"),
]