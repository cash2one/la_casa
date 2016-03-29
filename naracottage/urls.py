from django.conf.urls import url
from naracottage import views

urlpatterns = [
    url(r'^$', views.home),
]