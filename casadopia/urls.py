from django.conf.urls import url
from casadopia import views

urlpatterns = [
    url(r'^$', views.home)
]
