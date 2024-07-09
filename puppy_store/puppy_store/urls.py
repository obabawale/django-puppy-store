from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include('puppies.urls', namespace="puppies")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]