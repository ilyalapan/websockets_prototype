from django.conf.urls import url
from example.views import user_list, open_box


urlpatterns = [
    url(r'^$', user_list, name='user_list'),
    url(r'^open$', open_box, name='open'),
    url(r'^check_status$', open_box, name='open'),

]
