from django.contrib import admin
from .models import Menu


class NestedMenuInline(admin.TabularInline):
    model = Menu
    extra = 1

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'parent':
            kwargs['queryset'] = Menu.objects.filter(parent__isnull=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'parent')
    list_filter = ('parent',)
    inlines = [NestedMenuInline]

admin.site.register(Menu, MenuAdmin)
