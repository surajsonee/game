"""dashboard URL Configuration

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
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$', 'socialapp.views.home', name='home'),
	url(r'^news/$', 'socialapp.views.news', name='news'),
	url(r'^save_news/$', 'socialapp.views.save_news', name='save_news'),
	url(r'details/(\d+)$', 'socialapp.views.details', name='details'),
	#url(r'^news_detail/$', 'socialapp.views.news_detail', name='news_detail'),
]
