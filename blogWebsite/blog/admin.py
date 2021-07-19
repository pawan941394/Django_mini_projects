from django.contrib import admin
from .models import Post,BlogComment
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author']
    class Media:
      js= ('tiny.js',)

admin.site.register(BlogComment)


