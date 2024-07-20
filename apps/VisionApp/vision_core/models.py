from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userhash = models.CharField(max_length=100)
    activestatus = models.BooleanField(default=False)
    logintime = models.DateTimeField(null=True, blank=True)
    email = models.EmailField()
    class Meta:
        db_table = 'CV_User'
        verbose_name_plural = 'CV_User'
        
    def __str__(self): return str(self.id)


class CV_Dataset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # image_dataset = models.FileField(upload_to='image_datasets/')
    # model_file = models.FileField(upload_to='model_files/')
    training_status = models.BooleanField(default=False)
    trained_model_accuracy = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = 'CV_Dataset'
        verbose_name_plural = 'CV_Dataset'
        
    def __str__(self): return str(self.id)
