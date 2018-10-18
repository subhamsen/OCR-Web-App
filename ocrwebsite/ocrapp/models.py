from django.db import models

# Create your models here.
class OpticalCharacterRecognition(models.Model):
    text_image = models.ImageField(upload_to = 'media/',null = True, blank = True)
