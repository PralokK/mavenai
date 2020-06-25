from django.urls import path
from django.views.generic.base import RedirectView

from . import views

urlpatterns=[path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    ]


