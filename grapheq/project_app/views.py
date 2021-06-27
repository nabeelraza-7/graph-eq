from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'project_app/index.html')

def about_page(request):
    return render(request, "project_app/about_page.html")

def plot(request):
    equations_from_fields = request.POST.getlist('equation')
    image = request.POST.getlist('image_file')
    if len(equations_from_fields) != 0:
        plot_eq_fields(equations_from_fields)
        return render(request, 'project_app/results.html')
    elif len(image) != 0 :
        plot_eq_image(image)
        return render(request, 'project_app/results.html')
    return render(request, 'project_app/plot.html')
    

def plot_eq_fields(equations_from_fields):
    print("Equation here...", equations_from_fields)

def plot_eq_image(image):
    print("Image here...", image)

def show_results(request):
    return render(request, 'project_app/results.html')

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR Password is incorrect.')
    return render(request, 'project_app/user_login.html')

def user_logout(request):
    logout(request)
    return redirect('user_login')

def user_registration(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account successfully created for: " + user)
            return redirect('user_login')
        else:
            messages.error(request, "You filled the data wrong")
    context = {'form':form}
    return render(request, 'project_app/user_registration.html', context)