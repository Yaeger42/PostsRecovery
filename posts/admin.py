from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin"""

    list_display = ('id', 'user', 'title', 'body', 'created', 'lastUpdated')
    search_fields = ('title', 'user__username', 'user__email')
    list_filter = ('created', 'lastUpdated')
    list_display_links = ('id', 'title', 'body', 'user')