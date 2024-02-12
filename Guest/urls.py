from django.urls import path
from Guest import views
app_name= "webguest"
urlpatterns = [
    path('',views.login,name="login"),   
]