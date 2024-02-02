from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('signup',views.signup),
    path('signin',views.signin),
    path('dashboard/<uname>',views.dashboard),
    path('write/<uname>',views.write),
    path('fullblog/<int:id>',views.full_blog),
    path('logout',views.logout),
]