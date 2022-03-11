from django.contrib import admin
from .models import Page, Chapter

class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

class ChapterAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

# Register your models here.
admin.site.register(Page, PageAdmin)
admin.site.register(Chapter, ChapterAdmin)

title = "Panel de Administración IOSA | Aerolíneas Argentinas"
subtitle = "Panel de Gestión"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle