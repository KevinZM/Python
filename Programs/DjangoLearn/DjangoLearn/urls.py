"""DjangoLearn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from DjangoLearn.view import hello
from DjangoLearn.view import my_homepage_view
from DjangoLearn.view import date_time
from DjangoLearn.view import date_head

urlpatterns = [
    url(r'^hello/', hello),
    url('^$',my_homepage_view),
    url(r'^date_time/',date_time),
    url(r'^time/plus/(\d{1,2})/$',date_head),

]
