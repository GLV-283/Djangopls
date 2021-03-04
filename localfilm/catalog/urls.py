from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
]

urlpatterns += [
    path('', views.index, name='index'),
]

urlpatterns += [
    path('catalog/', include('catalog.urls')),
]