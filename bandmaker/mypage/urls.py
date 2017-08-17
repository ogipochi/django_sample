from django.conf.urls import url,include
from . import views
app_name = 'mypage'

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^edit/$',views.edit,name='edit'),
    url(r'^edit_confirm/$',views.edit_confirm,name='edit_confirm'),
    url(r'^edit_save/$',views.edit_save,name='edit_save'),
]