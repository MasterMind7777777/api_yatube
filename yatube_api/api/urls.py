from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views

from django.urls import include, path
from .views import PostViewSet, GroupViewSet, CommentViewSet

router = SimpleRouter()
router.register('api/v1/posts', PostViewSet)
router.register('api/v1/posts/<post_id>/comments', PostViewSet)
router.register('api/v1/groups', GroupViewSet)
router.register('api/v1/posts/<post_id>/comments/<comment_id>', CommentViewSet)

urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
]