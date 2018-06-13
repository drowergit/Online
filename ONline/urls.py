"""ONline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import xadmin
from Shopping.views import IndexView, LoginView,RegisterView, ActiveUserView,ResetpasswordView, ResetView, ModifyPwdView, LogoutView
from Shopping.views import PersonalView, UserinfoView, SafetyView,SafetyPassview, EmailView, SendEmailCodeView, SetpayView,\
    IdcardView, AddressView, NewAddressView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^login/', LoginView.as_view(), name="login"),
    url(r'^register/', RegisterView.as_view(), name="register"),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name="user_active"),
    # url(r'^reset/', ResetpasswordView.as_view(), name="reset_password"),
    url(r'^forget/', ResetpasswordView.as_view(), name="forget_pwd"),
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name="reset_pwd"),
    url(r'^modify_pwd/', ModifyPwdView.as_view(), name="modify_pwd"),
    url(r'^logout/', LogoutView.as_view(), name="logout"),
    url(r'^personal/', PersonalView.as_view(), name="personal"),
    url(r'^userinfo/', UserinfoView.as_view(), name="userinfo"),
    url(r'^safety/', SafetyView.as_view(), name="safety"),
    url(r'^password/', SafetyPassview.as_view(), name='pass'),
    url(r'^email/', EmailView.as_view(), name="email"),
    url(r'^sendemail_code/', SendEmailCodeView.as_view(), name="sendemail_code"),
    url(r'^setpay/', SetpayView.as_view(), name="setpay"),
    url(r'^idcard/', IdcardView.as_view(), name="idcard"),
    url(r'address/',AddressView.as_view(), name="address"),
    url(r'newadd/', NewAddressView.as_view(), name="newadd"),

]
