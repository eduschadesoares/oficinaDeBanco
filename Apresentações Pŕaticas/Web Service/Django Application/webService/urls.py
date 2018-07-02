import sys
sys.path.append('..')

from django.conf.urls import url, include
from rest_framework import routers
from API import views
from django.contrib import admin
from django.urls import include, path

"""router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
"""

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    # url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'', include('music.urls'), name='music'),
    path('admin/', admin.site.urls),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]