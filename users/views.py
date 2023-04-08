from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import secrets



def uploadImage(file):
    fs = FileSystemStorage()
    s=secrets.token_hex(10)
    filename =f"profile_images/{s}{file.name}"
    filename = fs.save(filename, file)
    return fs.url(filename)

@login_required
def editProfile(request):
    user = request.user

    if request.method == "POST":
        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        address = request.POST.get("address")
        profileImage = request.FILES.get("profileImage")

        p = ProfileForm(request.FILES)

        imagePath = uploadImage(profileImage)

     


        user.profile.firstName = firstName
        user.profile.lastName = lastName
        user.profile.address = address
        user.profile.profile_image = imagePath

        user.profile.save()

        messages.success(request, "User Profile saved")



    return render(request, "users/Profile.html")






