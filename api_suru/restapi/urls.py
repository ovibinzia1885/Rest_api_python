from django.urls import path
from restapi.views import Articlelist,AritleDetails #articlelist,aritical_detail
urlpatterns=[
    # path('articlelistapi/',articlelist,name='articlelist'),
    # path('aritical_detail/<int:pk>/',aritical_detail,name='aritical_detail'),

    path('Articlelist/',Articlelist.as_view(),name='Articlelist'),
    path('AritleDetails/<int:id>/',AritleDetails.as_view(),name='AritleDetails'),

]