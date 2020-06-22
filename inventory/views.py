from django.shortcuts import get_object_or_404, render
from django.template import loader

from .forms import ItemForm

# Create your views here.

from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect

from .models import Inventory

def index(request):
    latest_inventory_list = Inventory.objects.order_by('expiry_date')
    template = loader.get_template('inventory/index.html')
    context = {
        'latest_inventory_list': latest_inventory_list,
    }
    return HttpResponse(template.render(context, request))

def item_create(request):
    form = ItemForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('index'))
    return render(request, "inventory/form.html", {'form': form})
        

def detail(request, id):
    item = get_object_or_404(Inventory, pk=id)
    return render(request, 'inventory/detail.html', {'item': item})