from django.shortcuts import render, get_object_or_404, redirect
from .models import StationeryItem
from .forms import StationeryItemForm

def stationery_list(request):
    items = StationeryItem.objects.all()
    return render(request, 'inventory/stationery_list.html', {'items': items})

def stationery_detail(request, pk):
    item = get_object_or_404(StationeryItem, pk=pk)
    return render(request, 'inventory/stationery_detail.html', {'item': item})

def stationery_create(request):
    if request.method == 'POST':
        form = StationeryItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stationery_list')
    else:
        form = StationeryItemForm()
    return render(request, 'inventory/stationery_form.html', {'form': form})

def stationery_update(request, pk):
    item = get_object_or_404(StationeryItem, pk=pk)
    if request.method == 'POST':
        form = StationeryItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('stationery_list')
    else:
        form = StationeryItemForm(instance=item)
    return render(request, 'inventory/stationery_form.html', {'form': form})

def stationery_delete(request, pk):
    item = get_object_or_404(StationeryItem, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('stationery_list')
    return render(request, 'inventory/stationery_confirm_delete.html', {'item': item})
