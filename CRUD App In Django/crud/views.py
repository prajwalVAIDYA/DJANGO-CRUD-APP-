from django.shortcuts import render, redirect
from .models import Member

# Create your views here.

def index(request):
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'crud/index.html', context)

def create(request):
    member = Member(firstname=request.POST['firstname'], lastname=request.POST['lastname'])
    member.save()
    return redirect('/crud/')
    # return redirect('/')
    # if request.method == 'POST':
    #     member = Member(firstname=request.POST['firstname'], lastname=request.POST['lastname'])
    #     member.save()
    #     return redirect('/crud/')  # Redirect to the index after creation
    # return render(request, 'crud/base.html', {})  # Render the create form on GET

def edit(request, id):
    members = Member.objects.get(id=id)
    context = {'members': members}
    return render(request, 'crud/edit.html', context)

def update(request, id):
    member = Member.objects.get(id=id)
    member.firstname = request.POST['firstname']
    member.lastname = request.POST['lastname']
    member.save()
    return redirect('/crud/')

def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return redirect('/crud/')