from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show_view, name='show_view'),
    url(r'^post_data/$', views.post_data, name='post_data'),
]