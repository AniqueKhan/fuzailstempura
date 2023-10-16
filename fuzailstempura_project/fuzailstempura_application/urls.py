from django.urls import path
from fuzailstempura_application.views import index,contact_view

urlpatterns = [
    path("",index,name="index"),
    path("contact_view",contact_view,name="contact_view")
]
