from django.db import models
from django.conf import settings



class UserProfile(models.Model):
    phone = models.CharField(max_length=255,null=True,blank=True)
    birth_date = models.DateField(null=True,blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    
class Note(models.Model):
    COMPLETE_STATUS = [
    ('complete', 'Complete'),
    ('not_complete', 'Not Complete'),
]


    
    
    profile = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='notes')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255,choices=COMPLETE_STATUS,default='not_complete')
    
