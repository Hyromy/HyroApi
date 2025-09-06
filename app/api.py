from rest_framework import viewsets, permissions

from .models import Guild
from .serializers import GuildSerializer

class GuildViewSet(viewsets.ModelViewSet):
    queryset = Guild.objects.all()
    serializer_class = GuildSerializer
    permission_classes = [permissions.IsAuthenticated]
