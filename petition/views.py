from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import PetitonForm
from django.contrib import messages
from django.views.generic import UpdateView, CreateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Petitions
from django.urls import reverse




class ListPetitionView(LoginRequiredMixin,ListView):
    template_name ="petition/List.html"
    model =Petitions
    context_object_name="petitions"


    def get_queryset(self):
        return super(ListPetitionView, self).get_queryset().filter(created_by=self.request.user)




class CreatePetitionView(LoginRequiredMixin,CreateView,):
    template_name="petition/Create.html"
    form_class = PetitonForm
    model = Petitions


    



    def form_valid(self, form):
        self.object = form.save(False)
        self.object.created_by = self.request.user
        self.object.save()
        messages.success(self.request, "Petition created successfully")
        return HttpResponseRedirect(self.get_success_url())

    



class UpdatePetitionView(LoginRequiredMixin, UserPassesTestMixin,UpdateView,):
    template_name="petition/Update.html"
    form_class = PetitonForm
    model = Petitions
    context_object_name="petition"




    def post(self, *args, **kwargs):
        messages.success(self.request, "Petition Updated successfully")
        return super().post( *args, **kwargs)


    def test_func(self):
        return self.get_object().created_by == self.request.user
    



class DeletePetitionView(LoginRequiredMixin, UserPassesTestMixin,DeleteView,):
    template_name="petition/Delete.html"
    form_class = PetitonForm
    model = Petitions
    success_url="/petition/list/"




    def post(self, *args, **kwargs):
        messages.success(self.request, "Petition Deleted successfully")
        return super().post( *args, **kwargs)


    def test_func(self):
        return self.get_queryset()[0].created_by == self.request.user
    