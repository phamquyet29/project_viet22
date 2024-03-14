from django.contrib import admin
from django.urls import path
from posts import views as post_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_views.post_list, name='post_list'),
    path('post/<int:pk>/', post_views.post_detail, name='post_detail'),
    path('post/create/', post_views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', post_views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', post_views.post_delete, name='post_delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)