from django.conf.urls import url
from arbatflat import views

urlpatterns = [
    url(r'^$', views.home),
]
