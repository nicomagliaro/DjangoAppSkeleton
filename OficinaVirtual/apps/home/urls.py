from django.conf.urls import patterns,url
from OficinaVirtual.apps.home import views

urlpatterns = patterns('',
    url(r'^$',views.index_view,name='vista_principal'),
    url(r'^login/$',views.login_view,name='vista_login'),
    url(r'^registro/$',views.register_view,name='vista_registro'),
    url(r'^logout/$',views.logout_view,name='vista_logout'),
)
