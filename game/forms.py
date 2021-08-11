from django import forms
from django.db import models
from django.db.models import fields
from game.models import Game, Review


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ["name", "type", "photo", "desc"]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["game", "message"]
