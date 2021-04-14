from django.urls import path
from myapp import views
app_name="myapp"

urlpatterns = [
    path('',views.if_demo,name="if_demo"),
    path('ifelse/',views.ifelse_demo,name="ifelse_demo"),
    path('for/',views.for_demo,name="for_demo")
]