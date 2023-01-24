from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from apps.pateint.forms import PatientForm
from apps.pateint.models import patient


# Create your views here.
def pateintinfo(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('../pateint')
            except:
                pass

    else:
        form = PatientForm()
    return render(request, 'pateint/pateint.html', {'form': form})


def show(request):
    patients = patient.objects.all()

    context = {'patients': patients}

    html_template = loader.get_template('pateint/show.html')
    return HttpResponse(html_template.render(context, request))


def edit(request, id):
    patients = patient.objects.get(id=id)
    return render(request, 'pateint/edit.html', {'patients': patients})


def update(request, id):
    patients = patient.objects.get(id=id)
    form = PatientForm(request.POST, instance=patients)
    if form.is_valid():
        form.save()
        return redirect("../../pateint")
    return render(request, 'pateint/edit.html', {'patients': patients})


def destroy(request, id):
    patients = patient.objects.get(id=id)
    patients.delete()
    return redirect("../../pateint")
