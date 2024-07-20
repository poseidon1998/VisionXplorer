from rest_framework import serializers # type: ignore
from .models import UserProfile, CV_Dataset

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'userhash', 'activestatus', 'logintime', 'email']

class CV_DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CV_Dataset
        fields = '__all__'
