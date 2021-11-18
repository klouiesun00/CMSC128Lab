from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('recommendations/', views.recommendations_view, name='recs'),
    path('my-books/', views.mybooks_view, name='my-books'),
    path('lists/', views.lists_view, name='lists'),
    path('lists/top-books/', views.topbooks_view, name='top-books'),
    path('lists/for-you/', views.foryou_view, name='for-you'),
    path('lists/top-authors/', views.topauthors_view, name='top-authors'),
    path('lists/top-genres/', views.topgenres_view, name='top-genres')
]