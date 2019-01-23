from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import auth_login, auth_logout


app_name = 'account'


urlpatterns = [
    #url(r'^login/$', views.user_login, name='user_login'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='registration/login.html'), name='user_login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='user_logout'),
    url(r'^register/$', views.register, name="user_register"),
]