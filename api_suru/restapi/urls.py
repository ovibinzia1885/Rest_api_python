from django.urls import path
from restapi.views import articlelist,aritical_detail
urlpatterns=[
    path('articlelistapi/',articlelist,name='articlelist'),
    path('aritical_detail/<int:pk>/',aritical_detail,name='aritical_detail')

]