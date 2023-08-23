from django.contrib import admin

from .models import Modelis, Automobilis, Uzsakymas, Uzsakymoeil, Paslauga


@admin.register(Uzsakymas)
class UzsakymasAdmin(admin.ModelAdmin):
    list_display = ('id', 'data', 'suma', 'automobilis', 'status')
    list_filter = ('status',)
    search_fields = ('id', 'automobilis__klientas', 'automobilis__valstybinis_nr')

    class UzsakymoeilInline(admin.TabularInline):
        model = Uzsakymoeil
        extra = 1

    inlines = [UzsakymoeilInline]


admin.site.register(Modelis)
admin.site.register(Automobilis)
admin.site.register(Uzsakymoeil)
admin.site.register(Paslauga)
# Register your models here.
