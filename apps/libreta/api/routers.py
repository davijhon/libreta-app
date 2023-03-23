from rest_framework.routers import DefaultRouter
# from .views.general_views import *
from .views import PersonaViewSet, DireccionViewSet

router = DefaultRouter()

router.register(r'api/persona', PersonaViewSet, basename='persona')
router.register(r'api/direccion', DireccionViewSet, basename='direccion')


urlpatterns = router.urls