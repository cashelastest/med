from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from .forms import UserRegistrationForm, LoginForm, PostForm, zapysForm
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Post
from django_user_agents.utils import get_user_agent

home = 'http://127.0.0.1:8000/'


@login_required
def zapys(request):
    if request.method == 'GET':
        context= {'form': zapysForm()}
        return render(request, 'post_form.html', context)
    elif request.method == 'POST':
        form = zapysForm(request.POST)
        if form.is_valid():
            context= {'form': zapysForm()}
            form.save()
            return render(request, 'post_form.html', context)
        else:
            return render(request, 'post_form.html', {'form': form})    

@login_required  
def create_post(request):
    if request.method == 'GET':
        context= {'form': PostForm()}
        return render(request, 'post_form.html', context)
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            context= {'form': PostForm()}
            form.save()
            return render(request, 'post_form.html', context)
        else:
            return render(request, 'post_form.html', {'form': form})


def home(request):

    if request.user.is_authenticated:
        print('yes the user is logged-in')
    user_agent = get_user_agent(request)
    print(user_agent.is_pc)

    if user_agent.is_mobile:
        type = 'base_mobile.html'
        context={'user': request.user, 'type': type }
        return render(request, 'home.html', context)
    if user_agent.is_pc:
        type = 'base.html'
        context={'user': request.user, 'type': type }
        return render(request, 'home_pc.html', context)

@login_required
def dashboard1(request):
    posts = Post.objects.all()

    return render(request, 'dashboard.html', {'posts': posts})



def logouts(request):
    logout(request)
    return render(request, 'log_out.html')

def user_login(request):


    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(home)
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        user_agent = get_user_agent(request)
        form = LoginForm()
        if user_agent.is_mobile:
            type = 'base_mobile.html'
            context={'form': form, 'type': type }
            return render(request, 'login.html', context)
        if user_agent.is_pc:
            type = 'base.html'
            context={'form': form, 'type': type }
            return render(request, 'login.html', context)


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            date = user_form.cleaned_data['date']
            print(date)
            # Save the User object
            new_user.save()
            return render(request, 'dashboard.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'reg.html', {'user_form': user_form})
# Create your views here.
