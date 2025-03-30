from django.shortcuts import redirect, render

from contacts.forms import contactForm
from contacts.models import Contact

def home(request):
    query=request.GET.get('q','')
    contacts=Contact.objects.all()
    no_result=False
    if query:
        contacts=contacts.filter(name__icontains=query) | contacts.filter(email__icontains=query)
        if not contacts.exists():
            no_result=True
    return render(request,'home.html',{'contacts':contacts,'query':query,'no_result':no_result})


def add_contact(request):
    if request.method=='POST':
        form=contactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = contactForm()
    return render(request,'add_contact.html',{'form':form})


def edit_contact(request,id):
    contact=Contact.objects.get(id=id)
    if request.method=='POST':
        form=contactForm(request.POST,instance=contact)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=contactForm(instance=contact)
    return render(request,'edit_contact.html',{'form':form})


def delete_contact(request,id):
    contact=Contact.objects.get(id=id)
    if request.method=='POST':
        contact.delete()
        return redirect('home')
    return render(request,'delete_contact.html',{'contact':contact})