from django.shortcuts import render
from .models import Hotels
# Create your views here.
def hotel_block_view(request,*args,**kwargs):
    obj = Hotels.objects.get(id=1)
    context = {
        'name': obj.name,
        'location': obj.location,
        'Star': obj.star,
    }
    return render(request, "Hotels/hotel_block_view.html", context)