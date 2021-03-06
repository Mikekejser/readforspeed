from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('LoginView/', auth_views.login, name='login'),
    path('LogoutView/', auth_views.logout, name='logout'),
    path('oauth/', include('social_django.urls', namespace='social')),  # <--
]
