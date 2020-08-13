from django.contrib import admin
from .models import Post, CustomUser, Comment, Hashtag,Profile

# Register your models here.
admin.site.register(Post)
admin.site.register(CustomUser)
admin.site.register(Comment)
admin.site.register(Hashtag)
admin.site.register(Profile)
