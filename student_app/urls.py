from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('stud', views.stud_create, name='stud'),
    path('show', views.display, name='show'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.destroy, name='delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
