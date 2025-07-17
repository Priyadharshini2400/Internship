from django.contrib import admin
from .models import Ride,Post

# Register your models here.
admin.site.register(Ride) #un:django  #pwd:django123


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'published')
    list_filter  = ('published',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')
