from django.shortcuts import render , redirect
from .models import *

# Create your views here.

def receipes(request):
    if request.method=="POST":

        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')
        # print(receipe_name)
        # print(receipe_description)
        # print(receipe_image)

        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image,
        )
        return redirect('/')
    queryset= Receipe.objects.all()


    return render(request , 'receipes.html' , context={'page':"receipt page", 'receipes': queryset, })


def delete_receipe(request,id):
    queryset= Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/')

def update_receipe(request,id):
    queryset= Receipe.objects.get(id = id)

    if request.method=="POST":

        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        
        queryset.receipe_name = receipe_name,
        queryset.receipe_description = receipe_description,
        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect('/')
        

    return render(request , 'update_receipes.html' , context={'page':" Update Receipt page", 'receipe': queryset, })
