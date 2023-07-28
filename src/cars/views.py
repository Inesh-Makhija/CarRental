from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .forms import CarForm
from .models import Car

def car_create_view(request):
    context = {}
    form = CarForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        if request.user.is_authenticated:
            obj.user = request.user
            obj.save()
            return redirect('/cars/create/')
        form.add_error(None,"User must be logged in to create cars.")
    context['form'] = form
    return render(request, 'cars/create.html', context=context)

def car_list_view(request):
    object_list = Car.objects.all()
    return render(request, "cars/list.html", {"object_list" : object_list})


def car_detail_view(request, handle=None):
    obj = get_object_or_404(Car, handle=handle)
    is_owner = obj.user == request.user
    context = {}
    form = CarForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        if request.user.is_authenticated:
            obj.user = request.user
            obj.save()
            return redirect('/cars/create/')
        form.add_error(None,"User must be logged in to create cars.")
    context['form'] = form
    return render(request, 'cars/create.html', context=context)