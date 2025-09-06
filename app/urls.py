from rest_framework import routers

from app.api import (
    GuildViewSet
)

router = routers.DefaultRouter()

router.register(r'guild', GuildViewSet, basename = "guild")

urlpatterns = router.urls
