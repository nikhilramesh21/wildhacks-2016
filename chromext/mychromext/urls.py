# ./chromext/mychromext/urls.py

from django.conf.urls import url
from mychromext import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]