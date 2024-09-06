"""product_lead URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from prodleadflow.views import ProductViewSet, LeadCreateView, FetchLeadsBetweenTwoDates, Top10Products, Bottom10Products, ProductsCountByLead
from prodleadflow.frontend_views import (product_list, product_create, product_update, product_delete, lead_create, leads_between_dates, products_count_by_lead)

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    # Using frontend
    # Product Management
    url(r'^products/$', product_list, name='product_list'),
    url(r'^products/create/$', product_create, name='product_create'),
    url(r'^products/update/(?P<pk>\d+)/$', product_update, name='product_update'),
    url(r'^products/delete/(?P<pk>\d+)/$', product_delete, name='product_delete'),

    # Lead Management
    url(r'^leads/create/$', lead_create, name='lead_create'),

    # Reporting
    url(r'^leads-between-dates/$', leads_between_dates, name='leads_between_dates'),
    url(r'^products-count-by-lead/$', products_count_by_lead, name='products_count_by_lead'),

    # Using Postman
    url(r'^api/products/top10/$', Top10Products.as_view(), name='top_10_products'),
    url(r'^api/products/bottom10/$', Bottom10Products.as_view(), name='bottom_10_products'),

    url(r'^api/', include(router.urls)),
    url(r'^api/leads/$', LeadCreateView.as_view(), name='create_lead'),
    url(r'^api/leads/fetch-between-dates/$', FetchLeadsBetweenTwoDates.as_view(), name='fetch_leads_between_dates'),
    url(r'^api/leads/products-count/$', ProductsCountByLead.as_view(), name='products_count_by_lead'),

    # JWT Authentication
    url(r'^api/token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^api/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
]

