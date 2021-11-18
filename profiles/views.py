from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm, LogInForm, ProfileEditForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def sign_up(request):
    if request.method == "POST":
        if request.POST.get('submit2') == 'sign_up':
            signupform = SignUpForm(request.POST)
            try:
                user_exists = User.objects.get(username=request.POST['username'])   # get a user with same username
                signupform = SignUpForm()
                loginform = LogInForm()
                context = {
                    "form1": signupform,
                    "form2": loginform,
                    "invalid_un": True
                }
                return render(request, "profiles/Myprofile-before.html", context) 
            except User.DoesNotExist:
                if signupform.is_valid():
                    signupform.save()
                    return redirect("/home")  
        elif request.POST.get('submit1') == 'log_in':
            loginform = LogInForm(request.POST)
            if loginform.is_valid():                    # checks if data entered is valid (i.e. no empty textboxes)
                username = loginform.cleaned_data.get("username")
                password = loginform.cleaned_data.get("password")
                user = authenticate(request, username=username, password=password)
                if user != None:
                    request.session['user'] = username          # added session key for session handling
                    login(request, user)
                    return redirect("/home")        # redirect user to homepage
            signupform = SignUpForm()
            loginform = LogInForm()
            context = {
                "form1": signupform,
                "form2": loginform,
                "invalid_user": True
            }
            return render(request, "profiles/Myprofile-before.html", context)
    elif request.user.is_authenticated:
        return redirect("/my-profile")           
    signupform = SignUpForm()
    loginform = LogInForm()
    context = {
       "form1": signupform,
       "form2": loginform,
       "invalid_user": False
    }
    return render(request, "profiles/Myprofile-before.html", context)

@login_required
def user_profile(request):
    context = {
        "user" : request.user
    }
    return render(request, "profiles/Myprofile-after.html", context)

# removed login required decorator since try statemet already checks for valid users
def logout_view(request):
    try:
        del request.session['user']        # check if session can be deleted
    except KeyError:                            # if not, means anonymous user/session expiry
        context = {
        "user": request.user,
        "expired": True
    }
        return redirect("/session-expired")
        #return render(request, "profiles/logout.html", context)
    context = {                         # for sessions that didnt expire but user wants to log out
        "user": request.user,
        "expired": False
    }
    logout(request)
    return render(request, "profiles/logout.html", context)

def expired_session(request):
    context = {
        "user": request.user,
        "expired": True
    }
    return render(request, "profiles/logout.html", context)

@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect("/my-profile")
    else:
        form = ProfileEditForm(instance=request.user.profile) 
    context = {
        "form": form
    }
    return render(request, 'profiles/edit-profile.html', context)
    
