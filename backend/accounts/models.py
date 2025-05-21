from django.db import models
from django.conf import settings

class Role(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=124)

    def __str__(self):
        return self.code

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='profile',
        on_delete=models.CASCADE,
    )
    id_number = models.CharField(max_length=25, unique=True)
    phone = models.CharField(max_length=18)
    profession = models.CharField(max_length=56, blank=True)
    experience = models.TextField(blank=True)
    avatar = models.ImageField(
        upload_to='avatars',
        default='avatars/noavatar.png',
    )
    role = models.ManyToManyField(
        'accounts.Role',
        related_name='profiles',
        blank=True,
    )
    
    def __str__(self):
        return self.user.username
