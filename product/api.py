
from django.http import JsonResponse
from django.forms import ValidationError
from rest_framework import serializers, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from product.models import Image, Product, CATEGORY_CHOICES

class ChoiceField(serializers.ChoiceField):
    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 50

class ImageRelatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id','url']

class ProductSerializer(serializers.ModelSerializer):
    category = ChoiceField(choices=CATEGORY_CHOICES)
    images = ImageRelatedSerializer(many=True, required=False)

    class Meta:
        fields = ['id', 'ean', 'description', 'category', 'price', 'images']
        model = Product

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination

    @action(methods=['post'], detail=True)
    def add_image(self, request, pk=None):
        data = request.data

        result = { 
            'success': True, 
            'message':'Image created!' 
        }

        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            result['success'] = False
            result['message'] = 'Product doest not exist!'
            return JsonResponse(result, safe=False, status=404)

        try:
            image_url = data['image_url']
        except KeyError as e:
            result['success'] = False
            result['message'] = 'Missing field ' + str(e)
            return JsonResponse(result, safe=False, status=400)

        try:
            image = Image()
            image.url = image_url
            image.product = product
            image.full_clean()
            image.save()
        except ValidationError as e:
            result['success'] = False
            result['message'] = 'Validation error: ' + str(e)
            return JsonResponse(result, safe=False, status=400)

        return JsonResponse(result, safe=False, status=201)
    
    @action(methods=['delete'], detail=True)
    def delete_image(self, request, pk=None):
        data = request.data

        result = { 
            'success': True, 
            'message':'Image deleted!' 
        }

        try:
            image_id = data['image_id']
        except KeyError as e:
            result['success'] = False
            result['message'] = 'Missing field ' + str(e)
            return JsonResponse(result, safe=False, status=400)

        try:
            Image.objects.filter(id=int(image_id)).delete()
        except Exception as e:
            result['success'] = False
            result['message'] = 'Error to delete: ' + str(e)
            return JsonResponse(result, safe=False, status=500)

        return JsonResponse(result, safe=False, status=200)