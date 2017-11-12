"""Define mode for learning_logs"""
from django.conf.urls import url
from . import views

urlpatterns = [
    # index
    url(r'$', views.index, name='index'),
    # show all topics
    url(r'^topics/$', views.topics, name='topics'),
    # show the detail topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]