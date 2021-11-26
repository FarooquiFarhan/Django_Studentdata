from django.contrib import admin
from blog.models import Blog
from blog.models import Author
from blog.models import Entry

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
admin.site.register(Blog, BlogAdmin)
class AuthorAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
admin.site.register(Author, AuthorAdmin)
class EntryAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
admin.site.register(Entry, EntryAdmin)