from rest_framework import generics, permissions
from .models import Note
from .serializers import NoteSerializer, UserRegisterSerializer
from .permissions import IsOwnerOnly


class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]


class NoteListCreateView(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NoteDetailview(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOnly]

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)