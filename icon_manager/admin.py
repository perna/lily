from django.contrib import admin
from .models import Icon, IconFile

class IconFileInline(admin.TabularInline):
    model = IconFile
    extra = 2
    list_display = ['files__name']

class IconAdmin(admin.ModelAdmin):
    list_display = ['name', 'tags']
    list_filter = ['files__file_extension']
    search_fields = ('name', 'tags')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ IconFileInline ]


admin.site.register(Icon, IconAdmin)
