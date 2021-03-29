from django.urls import path
from notes.views import (
    NotesCreateView,
    ReadNotesView,
    ReadNoteByIdView,
    UpdateNoteView,
    DeleteNoteView
)

urlpatterns = [
    path('note/create', NotesCreateView.as_view(), name='create_note'),
    path('note/list', ReadNotesView.as_view(), name='read_note'),
    path('note/read', ReadNoteByIdView.as_view(), name='read_note_id'),
    path('note/update', UpdateNoteView.as_view(), name='update_note'),
    path('note/delete', DeleteNoteView.as_view(), name='delete_note')
]
