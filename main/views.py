from main.serializers import *
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from main.models import *
from drf_yasg.utils import swagger_auto_schema


class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


@swagger_auto_schema(tags=["Tags"])
class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]


class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]


class ExperienceListCreateView(generics.ListCreateAPIView):
    queryset = Experience_at.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticated]


class ExperienceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experience_at.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticated]


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]


class EducationListCreateView(generics.ListCreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticated]


class EducationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticated]
