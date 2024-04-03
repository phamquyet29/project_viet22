from django.contrib import admin
from django.urls import path
from posts import views as post_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_views.post_list, name='post_list'),
    path('post/<int:pk>/', post_views.post_detail, name='post_detail'),
    path('post/create/', post_views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', post_views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', post_views.post_delete, name='post_delete'),
     path('logout/', post_views.logout_view, name='logout'),
    path('login/', post_views.login_view, name='login'),
    path('register/', post_views.register_view, name='register'),
    path('search/', post_views.search_view, name='search_view'),


    path('post/<int:post_id>/comment/', post_views.add_comment_to_post, name='add_comment_to_post'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)