from django.contrib import admin
from django.urls import include, path
from funcionarios.views import list_funcionarios, view_funcionario, user_login, register_user, logout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('funcionarios/', list_funcionarios, name='list_funcionarios'),
    path('funcionarios/<int:funcionario_id>/', view_funcionario, name='view_funcionario'),
    path('login/', user_login, name='login'),
    path('register/', register_user, name='register'),
    path('logout/', logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

