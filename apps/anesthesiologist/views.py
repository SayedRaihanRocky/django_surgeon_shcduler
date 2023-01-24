from django.shortcuts import render, redirect
from apps.anesthesiologist.forms import AnesthesiologistForm
from apps.anesthesiologist.models import anesthesiologist


# Create your views here.
def anesthesiologistinfo(request):
    if request.method == "POST":
        form = AnesthesiologistForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('../anesthesiologist')
            except:
                pass

    else:
        form = AnesthesiologistForm()
    return render(request, 'anesthesiologist/anesthesiologist.html', {'form': form})


def show(request):
    anesthesiologists = anesthesiologist.objects.all()

    return render(request, "anesthesiologist/show.html", {'anesthesiologists': anesthesiologists})


def edit(request, id):
    anesthesiologists = anesthesiologist.objects.get(id=id)
    return render(request, 'anesthesiologist/edit.html', {'anesthesiologists': anesthesiologists})


def update(request, id):
    anesthesiologists = anesthesiologist.objects.get(id=id)
    form = AnesthesiologistForm(request.POST, instance=anesthesiologists)
    if form.is_valid():
        form.save()
        return redirect("../../anesthesiologist")
    return render(request, 'anesthesiologist/edit.html', {'anesthesiologists': anesthesiologists})

def destroy(request, id):
    anesthesiologists = anesthesiologist.objects.get(id=id)
    anesthesiologists.delete()
    return redirect("../../anesthesiologist")
