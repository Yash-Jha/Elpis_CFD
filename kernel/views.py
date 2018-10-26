from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import City, Year

from django.http import JsonResponse

from .pop_predictor import estimate

# Create your views here.

def logout(request):
    request.session['uname'] = ''
    return redirect('home')

def home(request):
    request.session.set_expiry(0)
    if request.method == "POST":
        form = LoginForm(request.POST)
        data = form.save(commit=False)
        if(form.is_valid()):
            if(data.username == 'admin' and data.password == 'password'):
                request.session['uname'] = 'admin' 

    if(('uname' not in request.session) or request.session['uname'] == ''):
        return render(request, 'home.html', {'login_form' : LoginForm, 'uname':'', 'page':'home'})
    else:
        return render(request, 'home.html', {'uname' : request.session['uname'], 'page':'home'})

def pop_loss(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        data = form.save(commit=False)
        if(form.is_valid()):
            if(data.username == 'admin' and data.password == 'password'):
                request.session['uname'] = 'admin' 

    if(('uname' not in request.session) or request.session['uname'] == ''):
        return render(request, 'pop_loss.html', {'login_form' : LoginForm, 'uname':'','page':'pop_loss'})
    else:
        return render(request, 'pop_loss.html', {'uname' : request.session['uname'],'page':'pop_loss','cities':City.objects.all(),'years':Year.objects.all()})

def clusters(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        data = form.save(commit=False)
        if(form.is_valid()):
            if(data.username == 'admin' and data.password == 'password'):
                request.session['uname'] = 'admin' 

    if(('uname' not in request.session) or request.session['uname'] == ''):
        return render(request, 'clusters.html', {'login_form' : LoginForm, 'uname':'','page':'clusters'})
    else:
        return render(request, 'clusters.html', {'uname' : request.session['uname'],'page':'clusters'})

def request_pop_data(request):
    magnitude = request.GET.get('magnitude', None)
    coords = request.GET.get('city', None)
    density = request.GET.get('density', None)

    data = {}
    data['estimate'] = estimate(magnitude,coords,density)

    return JsonResponse(data)
