
from django.urls import path, include
from . import views
from . import HodViews
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('register/', views.registerUser, name="register"),
    path('about/', views.about, name="about"),
    path('blog/', views.blog, name="blog"),
    path('contact/', views.contact, name="contact"),
    path('gallery/', views.gallery, name="gallery"),
    path('team/', views.team, name="team"),
    path('logout/', views.logout, name="logout"),
    path('dashboard/', HodViews.dashboard, name="dashboard"),


    path("petition/", include("petition.urls")),
    path("users/", include("users.urls")),

 


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
