from django.shortcuts import render, redirect
from apps.sergeon.models import Surgeon
from apps.sergeon.forms import SurgeonForm


# Create your views here.
def surgeoninfo(request):
    if request.method == "POST":
        form = SurgeonForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('../sergeon')
            except:
                pass

    else:
        form = SurgeonForm()
    return render(request, 'sergeon/surgeon.html', {'form': form})


def show(request):
    surgeons = Surgeon.objects.all()
    return render(request, "sergeon/show.html", {'surgeons': surgeons})


def edit(request, id):
    surgeons = Surgeon.objects.get(id=id)
    return render(request, 'sergeon/edit.html', {'surgeons': surgeons})


def update(request, id):
    surgeons = Surgeon.objects.get(id=id)
    form = SurgeonForm(request.POST, instance=surgeons)
    if form.is_valid():
        form.save()
        return redirect("../../sergeon")
    return render(request, 'sergeon/edit.html', {'surgeons': surgeons})


def destroy(request, id):
    surgeons = Surgeon.objects.get(id=id)
    surgeons.delete()
    return redirect("../../sergeon")
