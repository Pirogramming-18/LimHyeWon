from django.shortcuts import render,redirect

from django.http.request import HttpRequest
from movieSite.reviews.models import Review

# Create your views here.

def reviews_list(request:HttpRequest,*args, **kwargs):
    reviews=Review.objects.all()
    print(reviews)
    return render(request,"reviews/reviews_list.html",{"reviews":reviews})

def reviews_retrieve(request,pk,*args, **kwargs):
    review=Review.objects.all().get(id=pk)
    print(review)
    return render(request,"reviews/reviews_retrieve.html",{"review":review})

def reviews_create(request,*args, **kwargs):
    if request.method=="POST":
        Review.objects.create(
            title=request.POST["title"],
            release_year=request.POST["release_year"],
            genre=request.POST["genre"],
            star_rating=request.POST["star_rating"],
            running_time=request.POST["running_time"],
            content=request.POST["content"],
            director=request.POST["director"],
            actors=request.POST["actors"],
        )
        return redirect("/")
    
    return render(request,"reviews/reviews_create.html")

def reviews_edit(request,pk,*args, **kwargs):
    review=Review.objects.get(id=pk)
    if request.method=="POST":
        review.title=request.POST["title"]
        review.release_year=request.POST["release_year"]
        review.genre=request.POST["genre"]
        review.star_rating=request.POST["star_rating"]
        review.running_time=request.POST["running_time"]
        review.content=request.POST["content"]
        review.director=request.POST["director"]
        review.actors=request.POST["actors"]
        review.save()
        return redirect("/reviews/{}".format(review.id))
    return render(request,"reviews/reviews_edit.html",{"review":review})

