from django.urls import path
from application import views


urlpatterns = [
    path('', views.Home().index, name='index'),

    path('post', views.Post().post, name='post'),

    path('api', views.API.as_view(), name='api'),
    path('api/put/<str:id>', views.API.as_view(), name='put'),


]