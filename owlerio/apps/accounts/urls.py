from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required

from .views import DashboardView, LogOutView, SetEmailView, UpdateProfileView, EditEmailsView, DeleteEmailView

urlpatterns = patterns('',
    url(r'^$', login_required(DashboardView.as_view()), name='dashboard'),
    url(r'^logout/$', login_required(LogOutView.as_view()), name='logout'),
    url(r'^profile/$', login_required(DashboardView.as_view()), name='profile'), # for twitter callback
    url(r'^edit-preferences/$', login_required(UpdateProfileView.as_view()), name='edit-profile'),
    url(r'^edit-emails/$', login_required(EditEmailsView.as_view()), name='edit-emails'),
    url(r'^email/(?P<email>\d+)/delete$', login_required(DeleteEmailView.as_view()), name='delete-email'),
    url(r'^set-email/$', login_required(SetEmailView.as_view()), name='set-email'),
)
