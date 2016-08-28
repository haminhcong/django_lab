from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.nova_log_view),
    url(r'^summary/$', views.nova_log_view),  # good

]
