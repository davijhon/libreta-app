from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import  SpectacularSwaggerView, SpectacularAPIView


urlpatterns = [
    # DJANGO APP
	path('admin/', admin.site.urls),
    
	# API
	path('libreta/', include('apps.libreta.api.routers')),
    
	# API SCHEMA:
	path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
