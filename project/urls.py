"""login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from indexapp import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path

urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    path('All/', views.All),
    path('Hot/', views.Hot),
    path('Featured/', views.Featured),
    path('New/', views.New),
    path('addnew/', views.addnew),
    path('create/', views.adduser),
    path('login/', views.login),
    path('logout/', views.logout),
    path('detail/<int:productid>/', views.detail),
    path('news/',include('newsadmapp.urls')),
    path('search/', views.search),
    path('delete/<int:editid>/', views.delete),
    path('delete/<int:editid>/<str:deletetype>/', views.delete),
    path('userdetail/', views.userdetail),
    path('admin/', admin.site.urls),
    path('edit/<int:id>/', views.edit),
    path('authAccess/',views.authAccess),
    path('check_ok/<int:productid>/',views.check_ok),
    path('downloadpage/',views.downloadpage),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


