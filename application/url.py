from django.urls import path
from application import views


urlpatterns = [
    path('', views.Home().index, name='index'),

    path('post/js', views.Post().js, name='js'),
    path('post', views.Post().post, name='post'),
    path('update/<str:id>', views.Post().update, name='update'),
    path('delete/<str:id>', views.Post().delete, name='delete'),


    path('api', views.API.as_view(), name='api'),
    path('api/put/<str:id>', views.API.as_view(), name='put'),


]