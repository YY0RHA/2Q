from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Advertisements81
from .forms import Advertisements81Form
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

def index(request):
    advertisements = Advertisements81.objects.all()
    context = {'advertisements':advertisements}
    return render(request, 'app_advertisements81/index.html', context)

def top_sellers(request):
    return render(request, 'app_advertisements81/top-sellers.html')
@login_required(login_url=reverse_lazy('login'))
def advertisement_post(request):
    if request.method == "POST":
        form = Advertisements81Form(request.POST, request.FILES)
        if form.is_valid():
            new_advertisement = form.save(commit=False)
            new_advertisement.user = request.user
            new_advertisement.save()
            url = reverse('main-page')
            return HttpResponseRedirect(url)
    else:
        form = Advertisements81Form()
    context = {'form' : form}
    return render(request, 'app_advertisements81/advertisement-post.html', context)