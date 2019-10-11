from django.urls import path
from basic_app import views

# For template tagging
app_name = "basic_app"
# look under basic_app and find the url that matches
urlpatterns = [path("/relative", views.relative, name="relative"),
               path("/other", views.other, name="other"), ]
