from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Sum
from django.contrib.auth import authenticate, login, logout

from stinkomanlevels.main.models import *
from stinkomanlevels.main.forms import *

def activeUser(request):
    """
    touch the request's user if they are authenticated in order
    to update the last_activity field
    """
    if request.user.is_authenticated():
        request.user.get_profile().save() # set active date

def home(request):
    activeUser(request)

    new_levels = Level.objects.order_by("-date_created")[:10]
    top_levels = Level.objects.annotate(rating_value=Sum("ratings__value")).order_by('-rating_value')[:10]

    return render_to_response('home.html', locals(), context_instance=RequestContext(request))

def user(request):
    activeUser(request)
    return render_to_response('user.html', locals(), context_instance=RequestContext(request))

def upload(request):
    activeUser(request)
    return render_to_response('upload.html', locals(), context_instance=RequestContext(request))

def submit(request):
    activeUser(request)
    return render_to_response('submit.html', locals(), context_instance=RequestContext(request))

def register(request):
    activeUser(request)
    return render_to_response('register.html', locals(), context_instance=RequestContext(request))

def rate(request):
    activeUser(request)
    return render_to_response('rate.html', locals(), context_instance=RequestContext(request))

def post(request):
    activeUser(request)
    return render_to_response('post.html', locals(), context_instance=RequestContext(request))

def play(request):
    activeUser(request)
    return render_to_response('play.html', locals(), context_instance=RequestContext(request))

def namecheck(request):
    activeUser(request)
    return render_to_response('namecheck.html', locals(), context_instance=RequestContext(request))

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def user_login(request):
    err_msg = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username', ''), password=form.cleaned_data.get('password', ''))
            if user is not None:
                if user.is_active:
                    login(request, user)
                    url = '/'
                    if request.GET.has_key('next'):
                        url = request.GET['next']
                    return HttpResponseRedirect(url)
                else:
                    err_msg = 'Your account is disabled.'
            else:
                err_msg = 'Invalid login.'
    else:
        form = LoginForm()
    return render_to_response('login.html', {'form': form, 'err_msg': err_msg }, context_instance=RequestContext(request))

def edit(request):
    activeUser(request)
    return render_to_response('edit.html', locals(), context_instance=RequestContext(request))

def dashboard(request):
    activeUser(request)
    return render_to_response('dashboard.html', locals(), context_instance=RequestContext(request))

def confirm(request):
    activeUser(request)
    return render_to_response('confirm.html', locals(), context_instance=RequestContext(request))

def browse(request):
    activeUser(request)
    return render_to_response('browse.html', locals(), context_instance=RequestContext(request))

