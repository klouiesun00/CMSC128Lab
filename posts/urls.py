from django.urls import path

from . import views

urlpatterns = [
    path('make-post/', views.CreatePostView, name='make-post'),
]