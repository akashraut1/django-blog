from django.contrib import admin
from .models import Post
from .models import Profile

admin.site.register(Profile)
admin.site.register(Post)

# Register your models here.
