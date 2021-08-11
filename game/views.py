from django.shortcuts import render, redirect
from game import models
import game
from game.models import Game, Review, Video
from django.http import HttpRequest, HttpResponse
from game.forms import GameForm, ReviewForm
from django.contrib.auth.decorators import login_required


def game_list(request):
    qs = Game.objects.all()
    return render(
        request,
        "game/game_list.html",
        {
            "game_list": qs,
        },
    )


def game_detail(request: HttpRequest, pk):
    game = Game.objects.get(pk=pk)
    review_list = game.review_set.all()
    video_list = game.video_set.all()
    return render(
        request,
        "game/game_detail.html",
        {
            "game": game,
            "review_list": review_list,
            "video_list": video_list,
        },
    )


@login_required
def game_new(request: HttpRequest):
    game = Game.objects.all()
    if request.method == "POST":
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            game.author = request.user
            game = form.save(commit=False)
            game.save()
            return redirect(f"/game/")
    else:
        form = GameForm()

    return render(
        request,
        "game/game_form.html",
        {
            "form": form,
        },
    )


@login_required
def review_new(request: HttpRequest, pk):
    game = Game.objects.get(pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.game = game
            review.save()
            return redirect(game)
    else:
        form = ReviewForm()

    return render(
        request,
        "game/review_form.html",
        {
            "form": form,
        },
    )


@login_required
def review_edit(request: HttpRequest, review_pk, pk):
    game = Game.objects.get(pk=pk)
    review = Review.objects.get(pk=review_pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.game = game
            review.save()
            return redirect(game)
    else:
        form = ReviewForm(instance=review)

    return render(
        request,
        "game/review_form.html",
        {
            "form": form,
        },
    )


@login_required
def review_delete(request: HttpRequest, review_pk: int, pk: int) -> HttpResponse:
    game = Game.objects.get(pk=pk)
    review = Review.objects.get(pk=review_pk)
    if request.method == "POST":
        review.author = request.user
        review.game = game
        review.delete()  # DB에 즉시 DELTE 쿼리를 전달
        # return redirect(f"/actor/movie/{movie.pk}/")
        # return redirect("movie_list_detail", movie.pk)
        return redirect(game)

    return render(
        request,
        "game/game_confirm_delete.html",
        {
            "review": review,
        },
    )
