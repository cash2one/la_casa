from django.conf.urls import url
from naracottage import views

urlpatterns = [
    url(r'^$', views.home_ru),
    url(r'^ru/$', views.home_ru),
    url(r'^en/$', views.home_en),
]
