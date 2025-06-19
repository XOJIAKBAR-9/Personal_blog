from rest_framework import serializers
from main.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'slug', 'name']


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience_at
        fields = ['id', 'name', 'slug', 'description']


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'tags', 'content', 'created_at', 'reading_time']


class ProjectSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'owner', 'title', 'description', 'status', 'created_at', 'repo_link']


class EducationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Education
        fields = ['id', 'user', 'school_uni', 'degree', 'description', 'start_date', 'end_date']
