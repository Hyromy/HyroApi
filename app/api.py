from rest_framework import viewsets, permissions

from .models import Guild
from .serializers import GuildSerializer

class SafeMethodPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:  # GET, HEAD, OPTIONS
            return True
        return request.user and request.user.is_authenticated

class GuildViewSet(viewsets.ModelViewSet):
    queryset = Guild.objects.all()
    serializer_class = GuildSerializer
    permission_classes = [SafeMethodPermission]
