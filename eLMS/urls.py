from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main import views
from froala_editor import views as froala_views
from django.contrib.auth.models import User
from django.http import HttpResponse

# Custom function to create an admin user
def create_admin(request):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "navneet", "navneet")
        return HttpResponse("✅ Superuser created! You can now log in.")
    return HttpResponse("⚠️ Superuser already exists.")

admin.site.site_header = "eLMS Administration"
admin.site.site_title = "eLMS Administration Portal"
admin.site.index_title = "Welcome to eLMS Administration Portal"

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('student/', views.guestStudent, name='guestStudent'),
    path('teacher/', views.guestFaculty, name='guestFaculty'),
    path('', include('main.urls')),
    path('', include('discussion.urls')),
    path('', include('attendance.urls')),
    path('', include('quiz.urls')),
    path('froala_editor/', include('froala_editor.urls')),
    
    # Temporary route to create a superuser
    path("create-admin/", create_admin),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
