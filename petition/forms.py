from django import forms
from .models import Petitions




class PetitonForm(forms.ModelForm):
    title= forms.CharField(widget= forms.TextInput
                           (attrs={'class':'form-control ',"placeholder":"Petition Title"}),
                           label="Petition Title"
                           )
    
    description= forms.CharField(widget= forms.TextInput
                           (attrs={'class':'form-control', "placeholder":"Petition Description"}),
                           label="Petition Description"
                           )
    
    content= forms.CharField(widget= forms.Textarea
                           (attrs={'class':'form-control',"placeholder":"Petition Content"}),
                           label="Petition Content",
                           )
    class Meta:
        model = Petitions
        fields =["title", "description", "content"]
    
    