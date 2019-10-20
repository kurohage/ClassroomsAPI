
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views
#from classroomapi import views
from classroomapi.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),

    path('api/classroom/list/', ClassroomList.as_view()),
    path('api/classroom/create/', ClassroomCreate.as_view()),
    path('api/classroom/details/<int:classroom_id>/', ClassroomDetails.as_view()),
    path('api/classroom/update/<int:classroom_id>/', ClassroomUpdate.as_view()),
    path('api/classroom/delete/<int:classroom_id>/', ClassroomDelete.as_view()),

    path('login/', TokenObtainPairView.as_view(), name="login"),
]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
