import sys
from io import BytesIO

from PIL import Image
from django.contrib.auth.models import User
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from image_processing import thumbnail
from profileapp.tasks import generate_thumbnail_celery_lag


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    nickname = models.CharField(max_length=50, null=False)
    image = models.ImageField(upload_to='profile/', null=True, blank=True)
    thumb = models.ImageField(upload_to='profile/thumbnail', null=True)
    message = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def save(self, async_func=False,*args, **kwargs):
        if async_func:
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)
            generate_thumbnail_celery_lag.delay(self.pk)

    # def save(self, *args, **kwargs):
    #     self.generate_thumbnail()
    #     super().save(*args, **kwargs)
    # def generate_thumbnail(self):
    #     if self.image:
    #         output = generate_thumbnail_celery_lag.delay(self.image)
    #         self.thumb = InMemoryUploadedFile(output, "ImageField", self.image.name,
    #                                           'image/jpeg', sys.getsizeof(output), None)

# @receiver(post_save, sender=Profile)
# def async_generate_thumbnail(sender, instance=None, created=False, **kwargs):
#     generate_thumbnail_celery_lag.delay(instance.pk)