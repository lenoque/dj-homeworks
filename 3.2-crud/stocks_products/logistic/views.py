from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from .models import Product, Stock
from .serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filters = [filters.BaseFilterBackend]


    def get_queryset(self):
        queryset = super().get_queryset()
        products = self.request.query_params.get('products')
        if products:
            queryset = queryset.filter(products=products)
        return queryset
