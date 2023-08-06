from django.shortcuts import render, redirect

from .models import ContactForm


# Create your views here.
def home(request):

    d = ContactForm.objects.all()

    return render(request, 'index.html', {"d": d})


def insertdata(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        data = ContactForm(name=name, email=email, message=message)
        data.save()

        return redirect("/")


def delete(request, id):

    dd = ContactForm.objects.get(id=id)
    dd.delete()

    return redirect("/")

def editdata(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')

        edit = ContactForm.objects.get(id=id)
        edit.name = name
        edit.email = email

        edit.save()
        return redirect("/")

    ddd = ContactForm.objects.get(id=id)

    context = {"ddd": ddd}

    return render(request, 'edit.html', context)
