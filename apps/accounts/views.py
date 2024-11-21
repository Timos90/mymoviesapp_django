from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, AuthenticationForm

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts-urls:sign_in')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})

def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('movies-urls:home_page')
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/sign_in.html', {'form': form})

def sign_out(request):
    logout(request)
    return redirect('accounts-urls:sign_in')
