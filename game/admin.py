from django.contrib import admin
from game import models
from game.models import Game, Review, Video
from django.utils.safestring import mark_safe


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ["name", "type", "desc", "photo_image"]

    def photo_image(self, game: Game):
        html = f'<img src="{game.photo.url}"/>'
        return mark_safe(html)

    photo_image.short_description = "게임 이미지"


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["game", "message"]


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ["game", "title", "youtube_link"]

    def youtube_link(self, video: Video) -> str:
        html = f'<a href="{video.youtube_url}" target="_blank">바로보기</a>'
        return mark_safe(html)
