from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from lumia import views as lumia_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Ruta raíz → redirige al explore
    path('', lumia_views.explore_view, name='home'),
    
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html'
    ), name='login'),
    
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('register/', lumia_views.register_view, name='register'),
    path('explore/', lumia_views.explore_view, name='explore'),
    path('mapa/', lumia_views.mapa, name='mapa'),
]