from django import forms
from student_management_app.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =["profile_image",]