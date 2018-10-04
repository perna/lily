from django.contrib import admin
from .models import Icon, IconFile, IconType

class IconFileInline(admin.TabularInline):
    model = IconFile
    extra = 2
    list_display = ['files__name']

class IconAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ('name', 'tags')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ IconFileInline ]


class IconTypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Icon, IconAdmin)
admin.site.register(IconType, IconTypeAdmin)
