from django.shortcuts import render
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from Parsing.models import *
from Parsing.serializers import *


# Create your views here.


def categories(request):
    return render(request, 'categories.html')


class Index(GenericAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get(self, request):
        index = ProductSerializer(self.get_queryset(), many=True)
        context = {
            "object_list": index.data,
        }
        return render(request, 'index.html', context=context)
