from django.shortcuts import render
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny


from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter,SearchFilter

from django_filters.rest_framework import DjangoFilterBackend

from .filters import NotesFilter
from .paginations import Pagination
from .serializers import NoteSerializer,UserProfileSeializer,UpdateNoteSerializer
from .models import Note,UserProfile





class NoteViewSet(ModelViewSet):
    
    permission_classes = [IsAuthenticated]
    ordering_fields = ['created_at','title']
    pagination_class = Pagination
    filter_backends = [OrderingFilter,SearchFilter,DjangoFilterBackend]
    filterset_class = NotesFilter
    search_fields = ['title']

    def get_queryset(self):
        user = self.request.user
        
        return Note.objects.select_related('profile').filter(profile__user=user)
    
    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return UpdateNoteSerializer
        return NoteSerializer
    

    def perform_create(self, serializer):
        user = self.request.user
        # استرجاع البروفايل الخاص بالمستخدم
        profile = UserProfile.objects.get(user=user)
        # تمرير الـ profile إلى الـ serializer
        serializer.save(profile=profile)
        
   

    
    
    

class UserProfileViewset(ModelViewSet):
    http_method_names =['get','put','patch','head','option','delete']
    queryset = UserProfile.objects.select_related('user')
    serializer_class = UserProfileSeializer
    permission_classes = [IsAdminUser]
    
    
    
    
    @action(detail=False,methods=['GET','PUT'],permission_classes=[IsAuthenticated])
    def me(self,request):
        (profile,created) = UserProfile.objects.get_or_create(user_id=request.user.id)
        if request.method == 'GET':
            serializer = UserProfileSeializer(profile)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = UserProfileSeializer(profile,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
            
    