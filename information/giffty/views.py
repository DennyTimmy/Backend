from django.shortcuts import render

# Cr# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import InfoSerializer
from .models import Info

# Create your views here.


class informationApiView(RetrieveAPIView):
    serializer_class = InfoSerializer
    queryset = Info.objects.all()eate your views here.
