from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_user/user', UserView.as_view()),
    path('api_user/user/details/<int:pk>', UserDetailView.as_view()),

    path('api_tags/tags/', TagListCreateView.as_view()),
    path('api_tags/tags/<int:pk>/', TagDetailView.as_view()),

    path('api_experience/experiences/', ExperienceListCreateView.as_view()),
    path('api_experience/experiences/<int:pk>/', ExperienceDetailView.as_view()),

    path('api_post/posts/', PostListCreateView.as_view()),
    path('api_post/posts/<int:pk>/', PostDetailView.as_view()),

    path('api_projects/projects/', ProjectListCreateView.as_view()),
    path('api_projects/projects/<int:pk>/', ProjectDetailView.as_view()),

    path('api_edu/educations/', EducationListCreateView.as_view()),
    path('api_edu/educations/<int:pk>/', EducationDetailView.as_view()),
]

schema_view = get_schema_view(
    openapi.Info(
        title="My Blog",
        default_version='v1',
        description="For the personal blog project",
        contact=openapi.Contact(email="your@email.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
urlpatterns += [
    path('token/', token_obtain_pair),
    path('token/refresh/', token_refresh),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
