from rest_framework import viewsets
from housing.models import House
from housing.api.paginations import HousePagination
from serializers import BlogSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    pagination_class = HousePagination
    serializer_class = BlogSerializer
