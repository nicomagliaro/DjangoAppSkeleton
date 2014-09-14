from django.shortcuts import render_to_response
from django.template import RequestContext
from OficinaVirtual.apps.home.forms import ContactForm, LoginForm,RegisterForm
from django.core.mail import EmailMultiAlternatives # Enviamos HTML
from django.contrib.auth.models import User
import django
from OficinaVirtual.settings import URL_LOGIN
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
# Paginacion en Django
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.contrib.auth.decorators import login_required


def index_view(request):
    if not request.user.is_authenticated():
        return redirect('/login/?next=%s' % request.path)
    else:
        return render_to_response('home/index.html',context_instance=RequestContext(request))

def login_view(request):
    mensaje = ""
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                next = request.POST['next']
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                usuario = authenticate(username=username,password=password)
                if usuario is not None and usuario.is_active:
                    login(request,usuario)
                    return HttpResponseRedirect(next)
                else:
                    mensaje = "usuario y/o password incorrecto"
        next = request.REQUEST.get('next')
        form = LoginForm()
        ctx = {'form':form,'mensaje':mensaje,'next':next}
        return render_to_response('home/login.html',ctx,context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def register_view(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password_one = form.cleaned_data['password_one']
            password_two = form.cleaned_data['password_two']
            u = User.objects.create_user(username=usuario,email=email,password=password_one)
            u.save() # Guardar el objeto
            return render_to_response('home/thanks_register.html',context_instance=RequestContext(request))
        else:
            ctx = {'form':form}
            return  render_to_response('home/register.html',ctx,context_instance=RequestContext(request))
    ctx = {'form':form}
    return render_to_response('home/register.html',ctx,context_instance=RequestContext(request))
