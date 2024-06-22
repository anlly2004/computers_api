from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'marca', MarcaViewSet)
router.register(r'monitor', MonitorViewSet)
router.register(r'procesador', ProcesadorViewSet)
router.register(r'DiscoDuro', DiscoDuroViewSet)

urlpatterns =[
    path("api/v1/", include(router.urls))
]