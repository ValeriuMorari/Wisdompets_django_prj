from django.contrib import admin
from django.urls import path
from adoptions import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('adoptions/<int:pet_id>/', views.pet_detail, name='pet_detail')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
