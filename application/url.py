from django.urls import path
from application import views


urlpatterns = [
    path('', views.home().index, name='index'),

    path('api', views.API.as_view(), name='api'),
    path('api/put/<str:id>', views.API.as_view(), name='put'),


]