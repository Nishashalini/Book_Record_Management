from exam import views
from django.urls import re_path as url
urlpatterns=[
    url('test',views.showtest),
    url('result',views.showresult),
]
