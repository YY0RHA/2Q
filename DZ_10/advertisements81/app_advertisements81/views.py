from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Advertisements81
from .forms import Advertisements81Form
from django.urls import reverse
from django.http import HttpResponseRedirect

def index(request):
    advertisements = Advertisements81.objects.all()
    context = {'advertisements':advertisements}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisement_post(request):
    if request.method == "POST":
        form = Advertisements81Form(request.POST, request.FILES)
        if form.is_valid():
            new_advertisement = form.save(commit=False)
            new_advertisement = request.user
            new_advertisement.save()
            url = reverse('main-page')
            return HttpResponseRedirect(url)
    else:
        form = Advertisements81Form()
    context = {'form' : form}
    return render(request, 'advertisement-post.html', context)