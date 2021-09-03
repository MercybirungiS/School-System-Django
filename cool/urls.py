from cool.views import home
from django.urls import path
from django import views
from django.urls.conf import include
from django.urls.resolvers import URLPattern


urlpatterns=[
path ("" ,home,name="homepage")

]