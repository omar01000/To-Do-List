from rest_framework import serializers
from .models import Note,UserProfile

# 'user_create': 'djoser.serializers.UserCreateSerializer',





class NoteSerializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True)
    profile = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M",read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M",read_only=True)
    class Meta:
        model = Note
        fields = ['id','title','content','created_at','updated_at','profile','status']
        extra_kwargs = {
            'profile_id': {'read_only': True}
        }
    
class UpdateNoteSerializer(NoteSerializer):
    COMPLETE_STATUS = [
    ('complete', 'Complete'),
    ('not_complete', 'Not Complete'),
]
    status =serializers.ChoiceField(choices=COMPLETE_STATUS)
    class Meta(NoteSerializer.Meta):
        fields = ['id','title','content','created_at','updated_at','profile','status']
        
    

        
        

class UserProfileSeializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = UserProfile
        fields = ['id','user_id','phone','birth_date']
