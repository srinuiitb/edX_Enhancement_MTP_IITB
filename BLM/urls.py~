from django.conf.urls import patterns, url
from BLM import views


urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^hello/$', views.hello, name='hello'),
	url(r'^time/$', views.time_now, name='time_now'),
	url(r'^time/plus/(\d{1,2})/$', views.hours_ahead, name='hours_ahead'),
	url(r'^temp/$', views.current_datetime, name='current_datetime'),

)
