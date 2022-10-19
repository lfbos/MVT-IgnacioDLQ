from django.urls import path

from family import views

app_name = "family"
urlpatterns = [
    path("family", views.family, name="family-list"),
    path("create/<str:name>/<str:last_name>/<str:birthdate>/", views.create_family, name="family-create"),
]
