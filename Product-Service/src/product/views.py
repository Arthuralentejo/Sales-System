from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from .models import ProductModel
from .serializers import ProductSerializer
import logging

logger = logging.getLogger(__name__)


class Product(viewsets.ModelViewSet):
    queryset = ProductModel.objects.filter(active=True)
    serializer_class = ProductSerializer

    @action(detail=False, methods=["get"])
    def getByID(self, request):
        filter = request.query_params.get("filter")
        if filter:
            queryset = self.get_queryset().filter(filter)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        return Response({"error:filter isn't declarated"}, status=400)
