from django.urls import path
from app1 import views
from django.contrib import admin
from app1.models import FaceRecord
from django.views.generic import ListView
person_info={"queryset":FaceRecord.objects.all()}
urlpatterns = [
    path('admin/',admin.site.urls),
    path('', views.index, name='index'),
    path('register_person/', views.register_person, name='register_person'),
    path('success/', views.success, name='success'),
    path('face_tracking/', views.face_tracking, name='face_tracking'),
    path('person_records/',ListView.as_view(**person_info))
]
