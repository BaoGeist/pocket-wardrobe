from lib2to3.pygram import pattern_symbols
from turtle import back
from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Wardrobe
from .serializers import WardrobeSerializer
from .forms import PostForm
from . import eddie

# Create your views here.
@api_view(['GET'])
def getData(request): #Desired colour will be inputed
    items = Wardrobe.objects.filter(colour='orange',article='pants')
    serializer = WardrobeSerializer(items, many=True)
    return Response(serializer.data)

#def matchingColours(colour):
    #pass #

# Create your views here.

#outfit = [['orange','pants'],['blue','shirt'],['red','hat']]
def home(request):
    #res=[]
    #for piece in outfit:
        #clothing = Wardrobe.objects.filter(colour=piece[0],article=piece[1])
        #if clothing:
            #res.append(clothing)
    #context = {'piece': res}
    #print(context)

    return render(request, 'home/index.html')



#INpUT PAGE +==============

def input(request):
    form = PostForm()

    if request.method =='POST':
        form = PostForm(request.POST, request.FILES)
        print(request.FILES)
        #print(backend.process_colour(request.FILES['']))
        if form.is_valid():
            form.save()
        
    clothing = Wardrobe.objects.order_by('-pk')[0:3]
    
    print(clothing)

    context = {
        'form':form,
        'prev':clothing,
    }

    return render(request, 'home/input_page.html', context)


#Selected Fit page =========================================================================
def getFit(request):
    seek_rgb = eddie.eddie("Red")
    print(seek_rgb)
    queryset = Wardrobe.objects.none()
    for colour in seek_rgb:
        queryset |= Wardrobe.objects.filter(colour=colour)
    
    pants = queryset.filter(article='1')
    tops = queryset.exclude(article='1')
    
    if not pants:
        pants = Wardrobe.objects.none()
        pants |= Wardrobe.objects.filter(colour='black',article='1')

    selected_pant = pants.order_by('?').first()
    selected_top = tops.order_by('?').first()

    outfit = [selected_top, selected_pant]

    context ={
        'outfit': outfit
    }

    return render(request, 'home/generator.html', context)