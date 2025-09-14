from rest_framework import routers

from app.api import (
    GuildViewSet,
    ItemViewSet,
)

router = routers.DefaultRouter()

router.register(r'guild', GuildViewSet, basename = "guild")
router.register(r'item', ItemViewSet, basename = "item")

urlpatterns = router.urls
