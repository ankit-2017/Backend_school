from django.shortcuts import render
from django.http import *
from .models import *
from .forms import *
import os, tempfile, zipfile
from wsgiref.util import FileWrapper
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import get_user_model






def intro(request):

    print('hello')
    md='intro'
    return render(request, 'introduction.html', {'murl':md})

def registration(request, w):
    if request.method == 'POST':
        form1 = register(request.POST)
        if form1.is_valid():
            username = form1.cleaned_data['username']
            first_name = form1.cleaned_data['first_name']

            password = form1.cleaned_data['password']

            User.objects.create_user(username=username, password=password,first_name=first_name )
            usr = auth.authenticate(username=username, password=password)
            auth.login(request, usr)
            return HttpResponseRedirect ('/%s/%s/' %(w,w))

    else:
        form1 = register()

    return render(request, 'signup.html', {'form':form1} )

'''for home page'''

def registration_intro(request):
    if request.method == 'POST':
        form1 = register( request.POST )
        if form1.is_valid( ):
            username = form1.cleaned_data[ 'username' ]
            first_name = form1.cleaned_data[ 'first_name' ]

            password = form1.cleaned_data[ 'password' ]

            User.objects.create_user( username=username, password=password, first_name=first_name )
            usr = auth.authenticate( username=username, password=password )
            auth.login( request, usr )
            return HttpResponseRedirect ('/')

    else:
        form1 = register()

    return render(request, 'signup.html', {'form':form1} )



def login(request, w):

    if request.method == "POST":
        username = request.POST[ 'usr' ]
        password = request.POST[ 'pas' ]

        try:
            usr = auth.authenticate(username=username, password=password)
            print(usr)
            if usr is not None:
                auth.login( request, usr )
                return HttpResponseRedirect('/%s/%s/' %(w,w))
            else:

                messages.error( request, 'Email ID and password did not matched' )
                return HttpResponseRedirect( '/%s/%s/' % (w, w) )


        except:
            print( "invalid user" )

    return render( request, '%s.html' %w )


def login_intro(request):

    if request.method == "POST":
        username = request.POST[ 'usr' ]
        password = request.POST[ 'pas' ]

        try:
            usr = auth.authenticate(username=username, password=password)
            if usr is not None:
                auth.login( request, usr )
                return HttpResponseRedirect('/')
            else:

                messages.error( request, 'Email Id and password did not matched' )
                return HttpResponseRedirect( '/' )


        except:
            print( "invalid user" )

    return HttpResponseRedirect('/')



def logout(request, w):

    auth.logout(request)
    return HttpResponseRedirect('/%s/%s/' %(w,w))

def logout_intro(request):

    auth.logout(request)
    return HttpResponseRedirect('/')


# def django_tutorial_new(request, w):
#     #rk = django_url.objects.get(url=w)
#     pass









def windows(request):

    # if id == '64':
    #     filename = "D:\django\Backend\Files\python-3.5.3-amd64.zip"
    #     wrapper = FileWrapper(open(os.path.abspath(filename), 'rb'))
    #     response = HttpResponse(wrapper, content_type='text/plain')
    #     response['Content-Disposition'] = "attachment; filename=%s" % os.path.basename(filename)
    #     response['Content-Length'] = os.path.getsize(filename)
    #     return response

    # elif id == '32':
    #     filename = "D:\django\Backend\Files\python-3.5.4-win.zip"
    #     wrapper = FileWrapper(open(os.path.abspath(filename), 'rb'))
    #     response = HttpResponse(wrapper, content_type='text/plain')
    #     response['Content-Disposition'] = "attachment; filename=%s" % os.path.basename(filename)
    #     response['Content-Length'] = os.path.getsize(filename)
    #     return response
    # md='windows'
    return render(request, 'window_instal.html')


def linux(request):

    return render(request, 'linux.html')


def model1(request):

    # if w =='model' :
    #     filename = "D:\django\Backend\Files\student_project.zip"
    #     wrapper = FileWrapper( open( os.path.abspath( filename ), 'rb' ) )
    #     response = HttpResponse( wrapper, content_type='text/plain' )
    #     response[ 'Content-Disposition' ] = "attachment; filename=%s" % os.path.basename( filename )
    #     response[ 'Content-Length' ] = os.path.getsize( filename )

    #     return response

    # md = 'models'
    return render(request, 'models.html')


def myview(request):
    # if w == 'django_view':
    #     filename = "D:\django\Backend\Files\Tutorial.zip"
    #     wrapper = FileWrapper( open( os.path.abspath( filename ), 'rb' ) )
    #     response = HttpResponse( wrapper, content_type='text/plain' )
    #     response[ 'Content-Disposition' ] = "attachment; filename=%s" % os.path.basename( filename )
    #     response[ 'Content-Length' ] = os.path.getsize( filename )
    #     return response
    # md= 'views'
    return render(request, 'view.html')


def search_status(request):

    if request.method == "GET":
        search_text = request.GET['srch']
        if search_text is not None and search_text != u"":
            search_text = request.GET['srch']

            status = django_title.objects.filter( title__icontains=search_text)

        else:
            status = []

    return render(request, 'search_content.html', {'stats':status} )

def myforms(request):
    # if w=='download_form':
    #     filename = "D:\django\Backend\Files\Tutorial_form.zip"
    #     wrapper = FileWrapper( open( os.path.abspath( filename ), 'rb' ) )
    #     response = HttpResponse( wrapper, content_type='text/plain' )
    #     response[ 'Content-Disposition' ] = "attachment; filename=%s" % os.path.basename( filename )
    #     response[ 'Content-Length' ] = os.path.getsize( filename )
    #     return response
    # md='forms'
    return render(request, 'forms.html')

def bootstrap1(request):
    # if w=='bootstrap':
    #     filename = "D:\django\Backend\Files\Tutorial_bootstrap.zip"
    #     wrapper = FileWrapper( open( os.path.abspath( filename ), 'rb' ) )
    #     response = HttpResponse( wrapper, content_type='text/plain' )
    #     response[ 'Content-Disposition' ] = "attachment; filename=%s" % os.path.basename( filename )
    #     response[ 'Content-Length' ] = os.path.getsize( filename )
    #     return response
    # md= 'bootstrap_in_django'
    return render(request, 'bootstrap.html')

def combo(request):
    # if w=='combo1':
    #     filename = "D:\django\Backend\Files\Tutorial_views_combo.zip"
    #     wrapper = FileWrapper( open( os.path.abspath( filename ), 'rb' ) )
    #     response = HttpResponse( wrapper, content_type='text/plain' )
    #     response[ 'Content-Disposition' ] = "attachment; filename=%s" % os.path.basename( filename )
    #     response[ 'Content-Length' ] = os.path.getsize( filename )
    #     return response
    # md= 'combine_views'
    return render(request, 'more_views.html')
# Create your views here.

