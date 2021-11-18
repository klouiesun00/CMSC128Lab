from django.urls import path

from . import views

urlpatterns = [
    path('log-in-sign-up/', views.sign_up, name="sign-up"),
    path('my-profile/', views.user_profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('edit-profile/', views.edit_profile_view, name='edit'),
    path('session-expired/', views.expired_session, name='session-expired')
]