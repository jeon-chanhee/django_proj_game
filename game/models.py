from django.contrib.auth.models import User
from django.core.checks import messages
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.template.loader import render_to_string
from django.urls import reverse


class Game(models.Model):
    name = models.CharField(max_length=30, verbose_name="이름")
    type = models.CharField(max_length=20, verbose_name="장르")
    photo = models.ImageField(blank=True)
    desc = models.TextField(verbose_name="설명")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "게임"
        verbose_name_plural = "게임 List"

    def get_absolute_url(self) -> str:
        url = reverse("game_detail", args=[self.pk])
        # url = reverse("movie_detail",kwargs={"pk":self.pk})
        # return f"/movie/movies/{self.pk}" # 하드코딩
        return url


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=CASCADE)
    game = models.ForeignKey(Game, on_delete=CASCADE)
    message = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)


class Video(models.Model):
    game = models.ForeignKey(Game, on_delete=CASCADE)
    title = models.CharField(max_length=50)
    youtube_url = models.URLField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def youtube_embed_html(self):
        if "v=" in self.youtube_url:
            youtube_id = self.youtube_url.split("v=")[1]
            return render_to_string(
                "game/_youtube_embed.html",
                {
                    "youtube_id": youtube_id,
                },
            )
        return None
