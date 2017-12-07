from django.conf.urls import url, include
from . import views
from . import ajax
urlpatterns = [
    url(r'^$', views.index, name='main'),
    url(r'^ajax/createUser/$', ajax.create_user, name='createUser'),
    url(r'^ajax/show/$', ajax.show, name='showUser'),
    url(r'^ajax/getUserInfo/$', ajax.get_user_info, name='getUserInfo'),
    url(r'^ajax/checkBalance/$', ajax.check_balance, name='checkBalance'),
]