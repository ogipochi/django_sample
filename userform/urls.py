from django.conf.urls import url
import django.contrib.auth.views as auth_views
from . import views

app_name = 'userform'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^regist_user/$',views.regist_user,name='regist_user'),
    url(r'^regist_confirm/$',views.regist_confirm,name='regist_confirm'),
    url(r'^regist_save/$',views.regist_save,name='regist_save'),
     
]