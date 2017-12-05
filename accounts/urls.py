from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

app_name = 'account'

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}),
    url(r'^register/$', views.register, name='register'),
    url(r'^(?P<pk>[0-9]+)/$', views.ReservationView.as_view(), name='reservations'),
    url(r'^add/$', views.ReservationCreate.as_view(success_url="/account"), name='add'),
]