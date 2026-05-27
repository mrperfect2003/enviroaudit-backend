from rest_framework.routers import DefaultRouter

from .views import (
    ReviewItemViewSet
)

router = DefaultRouter()

router.register(
    r"",
    ReviewItemViewSet,
    basename="reviews"
)

urlpatterns = router.urls