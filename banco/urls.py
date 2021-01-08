
from django.contrib import admin
from django.urls import path, include
from conta.views import ContasViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Contas', ContasViewSet, basename='Contas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
