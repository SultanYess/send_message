from rest_framework import permissions, renderers, viewsets
from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .filters import SnippetFilter


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = SnippetFilter
    permission_classes = [permissions.IsAuthenticated]


    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
