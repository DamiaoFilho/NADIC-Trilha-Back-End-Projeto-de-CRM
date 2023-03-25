from rest_framework import viewsets

from crm.models import *
from .serializers import *

class stockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = stockSerializer