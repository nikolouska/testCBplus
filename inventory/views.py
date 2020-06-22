from django.shortcuts import get_object_or_404, render
from django.template import loader

# Create your views here.

from django.http import HttpResponse

from .models import Inventory


def index(request):
    latest_inventory_list = Inventory.objects.order_by('expiry_date')
    template = loader.get_template('inventory/index.html')
    context = {
        'latest_inventory_list': latest_inventory_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, id):
    item = get_object_or_404(Inventory, pk=id)
    return render(request, 'inventory/detail.html', {'item': item})