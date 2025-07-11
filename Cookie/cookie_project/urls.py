"""
URL configuration for cookie_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import include, path
from cookie.views import index, login_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login_view'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),  # 로그아웃 뷰
    path('cookie/', include('cookie.urls')),
    path('admin/', admin.site.urls),
]
