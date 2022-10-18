from django.urls import path

from family import views

app_name = "family"
urlpatterns = [
    path("family", views.family, name="family-list"),]
