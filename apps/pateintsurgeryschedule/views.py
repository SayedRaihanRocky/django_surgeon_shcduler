from django.shortcuts import render, redirect

from apps.pateintsurgeryschedule.forms import PateintSurgeryScheduleForm
from apps.pateintsurgeryschedule.models import pateingsurgeryscheduler
from apps.pateint.models import patient
from apps.sergeon.models import Surgeon
from apps.anesthesiologist.models import anesthesiologist


# Create your views here.


def create_pateintsurgeryschedule(request):
    # global
    pateintlist = patient.objects.all
    surgeonlist = Surgeon.objects.all
    anesthesiologistlist = anesthesiologist.objects.all

    if request.method == "POST":

        form = PateintSurgeryScheduleForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                return redirect('../pateintsurgeryschedule')
            except:
                pass

    else:
        form = PateintSurgeryScheduleForm()
    return render(request, 'pateintsurgeryschedule/pateintsurgeryschedule.html', {'form': form, 'pateints': pateintlist, 'surgeons': surgeonlist, 'anesthesiologists': anesthesiologistlist, })


def show(request):
    pateingsurgeryschedulers = pateingsurgeryscheduler.objects.all()

    return render(request, "pateintsurgeryschedule/show.html", {'pateingsurgeryschedulers': pateingsurgeryschedulers})


def edit(request, id):
    pateintlist = patient.objects.all
    surgeonlist = Surgeon.objects.all
    anesthesiologistlist = anesthesiologist.objects.all
    pateingsurgeryschedulers = pateingsurgeryscheduler.objects.get(id=id)
    return render(request, 'pateintsurgeryschedule/edit.html', {'pateingsurgeryschedulers': pateingsurgeryschedulers, 'pateints': pateintlist, 'surgeons': surgeonlist, 'anesthesiologists': anesthesiologistlist})


def update(request, id):
    pateingsurgeryschedulers = pateingsurgeryscheduler.objects.get(id=id)
    form = PateintSurgeryScheduleForm(request.POST, instance=pateingsurgeryschedulers)
    if form.is_valid():
        form.save()
        return redirect("../../pateintsurgeryschedule")
    return render(request, 'pateintsurgeryschedule/edit.html', {'pateingsurgeryschedulers': pateingsurgeryschedulers})

def destroy(request, id):
    pateingsurgeryschedulers = pateingsurgeryscheduler.objects.get(id=id)
    pateingsurgeryschedulers.delete()
    return redirect("../../pateintsurgeryschedule")
