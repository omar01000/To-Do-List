from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('notes',views.NoteViewSet,basename='notes')
router.register('profile',views.UserProfileViewset,basename='profile')


urlpatterns = router.urls
    

