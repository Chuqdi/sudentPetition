from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from student_management_app.models import CustomUser


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def classes(request):
    return render(request, 'class.html')


def gallery(request):
    return render(request, 'gallery.html')


def contact(request):
    return render(request, 'contact.html')


def blog(request):
    return render(request, 'blog.html')


def single(request):
    return render(request, 'single.html')


def team(request):
    return render(request, 'team.html')



def registerUser(request):
    data ={"email":""}
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirmPassword = request.POST.get("confirmPassword")
        data['email'] = email

        if password.upper() != confirmPassword.upper():
            messages.error(request, "Password does not match its confirmation")
            return redirect("register")

        user = CustomUser.objects.filter(email=email)

        if (user.exists()):
            messages.error(request, "User with this email already exists")
            return redirect("register")
        else:
            user = CustomUser()
            user.email = email
            user.user_type = 1
            user.set_password(password)
            user.save()
            messages.success(request, "Student account was created successfully")
            return redirect("login")



    return render(request, 'register.html', context=data)


def login(request):
    data ={ "email":""}
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        data['email'] = email
        
        user = CustomUser.objects.filter(email=email)

        if user.exists():
            user = user[0]
            if(user.check_password(password)):
                auth.login(request, user)
                return redirect("dashboard")
            else:
                messages.error(request, "Password Is Incorrect")
        else:
            messages.success(request, "User with this email does not exist")
         
    

    return render(request, "login.html", context=data)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login')

