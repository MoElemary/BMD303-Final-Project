
from django.urls import path
from . import views

app_name = "patient"
urlpatterns = [
    path("pat/", views.patient, name="pat"),
    path("pat/add/", views.add_patient, name="pat_add"),
    path("pat/ret/", views.ret_patient, name="pat_ret"),
    ]