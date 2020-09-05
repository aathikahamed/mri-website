from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('news-events/', views.news, name='news'),
    path('calendar/', views.calendar, name='calendar'),
    path('admission/', views.admission, name='admission'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('pregrade/', views.pregrade, name='pregrade'),
    path('primary/', views.primary, name='primary'),
    path('secondary/', views.secondary, name='secondary'),
    path('school-song/', views.school_song, name='school_song'),
    path('contact_api/', views.contact_api, name='contact_api'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
