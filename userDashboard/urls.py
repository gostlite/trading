from django.urls import path 
from .views import chart_view,home_page


urlpatterns=[
path("", home_page, name="home"),
path("dashboard/", chart_view, name="userDash")
]