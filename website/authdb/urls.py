from django.conf.urls import url

from . import views

urlpatterns = {
    url(r'^$', views.login_view, name='login'),
    url(r'^login/$', views.login_auth, name='login_auth'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^index/$', views.index, name='index'),
    url(r'^(?P<sid>[0-9]+)/$', views.details, name='details')
}