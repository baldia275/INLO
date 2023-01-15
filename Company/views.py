from django.shortcuts import render, redirect

from Company.models import Client
from django import forms


# Create your views here.
def clients(request):
    list_clients = Client.objects.all()
    return render(request, 'clients.html', {'clients': list_clients})


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name','age','username', 'address','town','country']


def inscription(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clients")

        else:
            print('Form not valid')

    else:
        form = ClientForm ()
    return render(request, 'inscription.html', {'form': form})