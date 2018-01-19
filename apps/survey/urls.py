from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^answer1$', views.answer1),
    url(r'^page2$', views.page2),
    url(r'^answer2$', views.answer2),
    url(r'^page1$', views.page1),
    
    
    
]
