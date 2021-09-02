from django import views
from django.conf.urls import url
from .views import CalendarView,event


app_name = 'calendaR'
urlpatterns = [

url('calender/',CalendarView.as_view(), name='CalenderView'),
url('event', event, name='event_new'),
url(r'^event/edit/(?P<event_id>\d+)/$', event, name='event_edit'),
]


    

