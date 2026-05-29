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
    path("perfil/", lumia_views.perfil, name="perfil"),
    path('register/', lumia_views.register_view, name='register'),
    path('explore/', lumia_views.explore_view, name='explore'),
    path('map/', lumia_views.mapa, name='map'),
    path('explore/parks/', lumia_views.parques_view, name='parks'),
    path('explore/parks/<str:park_name>/', lumia_views.park_detail_view, name='park_detail'),
]