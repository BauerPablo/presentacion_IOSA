from django.contrib import admin
from .models import Isarp, ChapterIsarp

class IsarpAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

class ChapterAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

# Register your models here.
admin.site.register(Isarp, IsarpAdmin)
admin.site.register(ChapterIsarp, ChapterAdmin)