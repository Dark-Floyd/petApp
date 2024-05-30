
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from pets import views

router = DefaultRouter()
router.register('pets', views.PetViewSet)


app_name = 'pets'

urlpatterns = [
    path('', include(router.urls)),
]
