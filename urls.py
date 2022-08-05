"""Recipe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from myRecipe import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myRecipe.urls')),
    # path('recipes/', include('myRecipe.urls')),
    path('user/', include('user.urls')),
    path('summernote/', include('django_summernote.urls')),
    #參考網址 https://blog.twshop.asia/django-%E6%89%80%E8%A6%8B%E5%8D%B3%E6%89%80%E5%BE%97-%E5%AF%8C%E6%96%87%E6%9C%AC%E7%B7%A8%E8%BC%AF%E5%99%A8-ckeditor/
    # path('ckeditor/', include('ckeditor_uploader.urls')),

    # 以下django內建的auth_views for reset password
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='reset_password.html'),
         name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='reset_password_sent.html'),
         name="password_reset_done"),
    path('user/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='reset.html'),
         name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='reset_password_complete.html'),
         name='password_reset_complete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)