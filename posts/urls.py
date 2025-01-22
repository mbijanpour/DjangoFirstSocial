from django.urls import path

from .views import *

app_name = 'posts'
urlpatterns = [
    path('<int:post_id>/<str:post_slug>/',
         PostDetailView.as_view(), name='post_detail'),
]
