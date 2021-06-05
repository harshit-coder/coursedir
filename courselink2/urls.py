"""courselink2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from quiz.views import *
from courselink2 import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', home),
                  path('start_quiz/<qid>/', quiz_view, name="quizview"),
                  path('start_quiz/<pk>/quiz/', quiz_data_view, name="quizdataview"),
                  path('start_quiz/<pk>/save/', quiz_data_save, name="quizdatasave"),
                  path('more_courses/', morecourse, name="morecourses"),
                  path('start_quiz/<pok>/<score>/result', calc, name="calculation"),
                  path('contact/', cont, name="contact")
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_title = 'Coursedir'
admin.site.site_header = 'Coursedir'
admin.site.index_title = 'Coursesir'
