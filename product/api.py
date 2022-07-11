
from rest_framework import serializers, viewsets
from rest_framework.pagination import PageNumberPagination

from product.models import Product, CATEGORY_CHOICES

class ChoiceField(serializers.ChoiceField):
    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 50

class ProductSerializer(serializers.ModelSerializer):
    category = ChoiceField(choices=CATEGORY_CHOICES)

    class Meta:
        fields = ['id', 'ean', 'description', 'category', 'price']
        model = Product

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination