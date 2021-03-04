from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
]

urlpatterns = [
     path('', views.index, name='index'),
]

urlpatterns = [
    path('', views.index, name='index'),
    path('filmini/', views.filminiListView.as_view(), name='filmini'),
    path('filmini/<int:pk>', views.filminiDetailView.as_view(), name='filmini-detail'),
]

# urlpatterns += [
#       path('catalog/', include('catalog.urls')),
# ]