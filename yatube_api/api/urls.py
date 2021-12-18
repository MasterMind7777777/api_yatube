from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views

from django.urls import include, path
from .views import PostViewSet, GroupViewSet, CommentViewSet, UserViewSet

router = SimpleRouter()
router.register('posts', PostViewSet)
router.register('posts/<post_id>/comments', PostViewSet)
router.register('groups', GroupViewSet)
router.register(r'users', UserViewSet)
router.register('posts/<post_id>/comments/<comment_id>', CommentViewSet)

urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('api/v1/', include(router.urls)),
]