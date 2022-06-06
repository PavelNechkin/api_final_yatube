from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = 'api'

router_for_v1 = routers.DefaultRouter()
router_for_v1.register('posts', PostViewSet, basename='posts')
router_for_v1.register('groups', GroupViewSet, basename='groups')
router_for_v1.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)
router_for_v1.register('follow', FollowViewSet, basename='follow')


urlpatterns = [
    path('v1/', include(router_for_v1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
