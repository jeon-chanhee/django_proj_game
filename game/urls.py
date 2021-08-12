from django.urls import path
from game import views

urlpatterns = [
    path("", views.game_list, name="game_list"),
    path("<int:pk>", views.game_detail, name="game_detail"),
    path("new/", views.game_new, name="game_new"),
    path("<int:pk>/review/new/", views.review_new, name="review_new"),
    path(
        "<int:pk>/review/<int:review_pk>/edit/", views.review_edit, name="review_edit"
    ),
    path(
        "<int:pk>/review/<int:review_pk>/delete/",
        views.review_delete,
        name="review_delete",
    ),
]
