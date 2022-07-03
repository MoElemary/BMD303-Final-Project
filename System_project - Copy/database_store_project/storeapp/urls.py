from django.urls import include, path

from . import views

urlpatterns = [path("", views.homepage, name="homepage_user"),
               path("about-us/", views.about_us, name="information"),
               path("Patient/", views.Patient, name="Patient"),
               path("Details/", views.details, name="details"),
               path("pat/", views.patient, name="pat"),
               path("pat/add/", views.add_patient, name="pat_add"),
               path("pat/ret/", views.ret_patient, name="pat_ret"),
               # path("Admin_page/", views.Admin_view, name="admin_view"),
               ]
