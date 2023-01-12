from django.urls import path
from movieSite.apps.review.views import reviews_list

urlpatterns = [
    path("",reviews_list),
]
