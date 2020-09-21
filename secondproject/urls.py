"""secondproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from secondapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.aboutpage,name='about'),
    path('contact/',views.contactpage,name='contact'),
    path('signup/',views.register,name='register'),
    path('check_user/',views.check_user,name='check_user'),
    path('user_login/',views.user_login,name='user_login'),
    path('student_dash/',views.student_dash,name='student_dash'),
    path('teacher_dash/',views.teacher_dash,name='teacher_dash'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('exam_page/',views.exam_page,name='exam_page'),
    path('change_password/',views.change_password,name='change_password'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
