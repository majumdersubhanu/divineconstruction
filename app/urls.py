from django.conf.urls.static import static
from django.urls import path

from app import views
from divineConstruction import settings

app_name = 'divineConstruction'
urlpatterns = [
                  path('home/', views.index, name='index'),
                  path('about/', views.about, name='about'),
                  path('projects/', views.projects, name='projects'),
                  path('contact/', views.contact, name='contact'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)