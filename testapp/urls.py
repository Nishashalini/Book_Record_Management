from testapp import views
from django.urls import re_path as url
urlpatterns=[
   url('about',views.about),
   url('contact',views.showcontact),
   url('employee',views.employee_info_view),
   url('^$',views.greeting),
]
