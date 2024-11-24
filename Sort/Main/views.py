from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from Parsing.models import *
from Parsing.serializers import *
import django_filters.rest_framework
from rest_framework import filters


# Create your views here.


def categories(request):
    return render(request, 'categories.html')


class Filtering(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["category", ]
    search_fields = ["name", ]


class FilteringLower(ListAPIView):
    queryset = Product.objects.all().order_by("price")
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["category", ]


class FilteringHigher(ListAPIView):
    queryset = Product.objects.all().order_by("-price")
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["category", ]


class Index(GenericAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get(self, request):
        index = ProductSerializer(self.get_queryset(), many=True)
        context = {
            "object_list": index.data,
        }
        return render(request, 'index.html', context=context)


class Product(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get(self, request):
        index = ProductSerializer(self.get_queryset(), many=True)
        context = {
            "object_list": index.data,
        }
        return render(request, 'product.html', context=context)
