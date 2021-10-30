from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls',
         namespace='rest_framework')),  # <- add
    path('', include('user.urls')),  # <- add
    path('', include('messenger.urls'))
]
