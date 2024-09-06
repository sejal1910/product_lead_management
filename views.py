# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Count
from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from datetime import datetime
from .models import Product, Lead
from .serializers import ProductSerializer, LeadSerializer

from django.utils.dateparse import parse_datetime
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class LeadCreateView(generics.CreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [AllowAny]

# Reporting APIs
class FetchLeadsBetweenTwoDates(APIView):
    def get(self, request):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        if not start_date or not end_date:
            return Response({"error": "Both start_date and end_date are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
        except ValueError:
            raise ValidationError("Invalid date format. Please use 'YYYY-MM-DD'.")

        if start_date > end_date:
            raise ValidationError("Start date must be before end date.")

        if not start_date or not end_date:
            return Response({"error": "Invalid date format"}, status=status.HTTP_400_BAD_REQUEST)

        leads = Lead.objects.filter(created_at__range=(start_date, end_date))
        serializer = LeadSerializer(leads, many=True)
        return Response(serializer.data)

class Top10Products(APIView):
    def get(self, request):
        products = Product.objects.annotate(num_leads=Count('leads')).order_by('-num_leads')[:10]
        serializer = ProductSerializer(products, many=True)
        print(serializer.data)
        return Response(serializer.data)

class Bottom10Products(APIView):
    def get(self, request):
        products = Product.objects.annotate(num_leads=Count('leads')).order_by('num_leads')[:10]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductsCountByLead(APIView):
    def get(self, request):
        leads = Lead.objects.annotate(num_products=Count('interested_product'))
        lead_data = [{"lead_id": lead.id, "num_products": lead.num_products} for lead in leads]
        return Response(lead_data)
    