from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Lead
from .forms import ProductForm, LeadForm
from django.utils.dateparse import parse_date

def product_list(request):
    products = Product.objects.all()
    return render(request, 'prodleadflow/product_list.html', {'products': products})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'prodleadflow/product_form.html', {'form': form})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'prodleadflow/product_form.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'prodleadflow/product_confirm_delete.html', {'product': product})

def lead_create(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = LeadForm()
    return render(request, 'prodleadflow/lead_form.html', {'form': form})

def leads_between_dates(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    if start_date and end_date:
        start_date = parse_date(start_date)
        end_date = parse_date(end_date)
        leads = Lead.objects.filter(created_at__range=[start_date, end_date])
    else:
        leads = Lead.objects.all()
    return render(request, 'prodleadflow/leads_between_dates.html', {'leads': leads})

def products_count_by_lead(request):
    leads = Lead.objects.all()
    return render(request, 'prodleadflow/products_count_by_lead.html', {'leads': leads})
