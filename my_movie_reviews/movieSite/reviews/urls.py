from django.urls import path
from movieSite.reviews.views import reviews_list,reviews_retrieve,reviews_create,reviews_edit,reviews_delete

urlpatterns = [
    path("",reviews_list),
    path("reviews/create",reviews_create),
    path("reviews/<int:pk>",reviews_retrieve),
    path("reviews/<int:pk>/delete",reviews_delete),
    path("reviews/<int:pk>/edit",reviews_edit),
]
