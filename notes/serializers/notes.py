from rest_framework import serializers
from notes.models import NoteModel
from django.db.models import Q

class NotesSerializerModel(serializers.ModelSerializer):

    class Meta:
        model = NoteModel
        fields = '__all__'


class NotesCreateSerializer(serializers.Serializer):

    user = serializers.EmailField(required=True)

    title = serializers.CharField(max_length=255)

    content = serializers.CharField(max_length=400, trim_whitespace=True)

    is_public = serializers.BooleanField(required=False, default=False)

    def create(self, data):
        note = NoteModel.objects.create(**data)
        return NotesSerializerModel(note).data

class ReadNotesSerializer(serializers.Serializer):

    user = serializers.EmailField(required=True)

    is_public = serializers.BooleanField(required=False, default=False)

    def create(self, data):
        notes = NoteModel.objects.filter(
            Q(user=data['user'])|
            Q(is_public=data['is_public']))
        return NotesSerializerModel(notes, many=True).data


class ReadNoteByIdSerializer(serializers.Serializer):

    id = serializers.IntegerField(required=True)

    def create(self, data):
        note = NoteModel.objects.filter(id=data['id'])
        return NotesSerializerModel(note).data


class UpdateNoteSerializer(serializers.Serializer):

    user = serializers.EmailField(required=True)

    id = serializers.IntegerField(required=True)

    def create(self, data):
        note = NoteModel.objects.filter(
            user=data['user'],
            id=data['id']
        ).update(**data)
        return note


class DeleteNoteSerializer(serializers.Serializer):

    user = serializers.EmailField(required=True)

    id= serializers.IntegerField(required=True)

    def create(self, data):
        note = NoteModel.objects.filter(
            user=data['user'],
            id=data['id']
        )
        if note[0] != data['id']:
            return False
        return True
