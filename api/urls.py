from rest_framework import routers
from django.conf.urls import include, url, patterns
from housing.api.views import HouseViewSet
from distance.api.views import DistanceViewSet
from department.api.views import DepartmentViewSet

router = routers.DefaultRouter()
router.register(r'house', HouseViewSet, base_name='house')
router.register(r'distance', DistanceViewSet, base_name='distance')
router.register(r'department', DepartmentViewSet, base_name='department')

app_name = 'api'

urlpatterns = patterns(
    'api',
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
)
