from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', auth_views.login, {'template_name': 'analyze/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^test/(?P<string>[\w\-]+)/$', views.test, name='test'),
    url(r'', views.home, name='home'),
    url(r'^settings.STATIC_URL + "deniz_graph.png"', views.show_sentiment_graph,
        name='show_sentiment_graph'),
]

#
