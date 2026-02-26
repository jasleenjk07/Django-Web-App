from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse
from app.models import Note

'''def LPU(req):
    return HttpResponse("LPU is the best university in World.")
def aboutLPU(req):
    return HttpResponse("LPU is one of India's Largest Private universities, located in punjab.")
def L(req):
    return HttpResponse("L for lion")
def claas(req):
    return HttpResponse("The learning environment in lpu is very interactive and interesting")'''

def home(req):
    notes = Note.objects.all()
    return render(req, "index.html", context={'notes':notes})
def deleteview(req,id):
    note=Note.objects.get(id=id)
    note.delete()
    messages.success(req,"notedeleted")
    return redirect("/")

def about(req):
    return render(req, "about.html")

def save_data(req):
    if req.method == "POST":
        title = req.POST.get("title", "").strip()
        description = req.POST.get("description", "").strip()

        if not title or not description:
            messages.error(req, "Fill all details")
            return redirect("/")

        note = Note(title=title, description=description)
        note.save()

        messages.success(req, "Details saved successfully")

    return redirect("/")

def update_note(req,id):
    note=Note.objects.get(id=id)
    return render(req,"edit_page.html",{"note":note})

def updateDataView(req, id):

    note = Note.objects.get(id=id)

    title = req.POST.get("title", "")
    description = req.POST.get("description", "")

    if not title or not description:
        messages.error(req, "Fill all details")
        return redirect(f"/update-note/{id}")

    note.title = title
    note.description = description
    note.save()

    messages.success(req, "Note Updated Successfully")
    return redirect("/")