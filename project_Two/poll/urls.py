from django.conf.urls import url
from poll import views


urlpatterns = [
    url(r'^$', views.helpme, name='help')
]
