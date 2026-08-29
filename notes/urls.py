from django.urls import path
from .views import NoteListCreateView, NoteDetailview, UserRegisterView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('notes/', NoteListCreateView.as_view(), name='note-list-create'),
    path('notes/<int:pk>/', NoteDetailview.as_view(), name='note-detail'),
]
