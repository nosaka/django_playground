from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^plan/$', views.plans, name='plans'),
    url(r'^plan/post/$', views.plan_post, name='plan_post'),
]