from django.contrib import admin
from .models import Icon, IconFile, IconType

class IconAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class IconFileAdmin(admin.ModelAdmin):
    list_display = ('icon', 'file_extension')
    list_filter = ('file_extension', 'icon')

class IconTypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Icon, IconAdmin)
admin.site.register(IconFile, IconFileAdmin)
admin.site.register(IconType, IconTypeAdmin)
