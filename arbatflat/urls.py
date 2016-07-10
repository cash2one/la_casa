from django.conf.urls import url
from arbatflat import views

urlpatterns = [
    url(r'^$', views.home_ru),
    url(r'^ru/$', views.home_ru),
    url(r'^en/$', views.home_en),
]
