from django.shortcuts import render

from django.http.request import HttpRequest
from movieSite.apps.review.models import Review

# Create your views here.

def reviews_list(request:HttpRequest,*args, **kwargs):
    reviews=Review.objects.all()
    print(reviews)
    return render(request,"templates/reviews_list.html",{"reviews":reviews})