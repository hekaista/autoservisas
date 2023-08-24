from django.contrib import admin

from .models import Modelis, Automobilis, Uzsakymas, Uzsakymoeil, Paslauga


@admin.register(Uzsakymas)
class UzsakymasAdmin(admin.ModelAdmin):
    # Padaryti, kad užsakymų sąraše būtų matomi automobilio ir datos stulpeliai
    list_display = ('data', 'suma', 'automobilis', 'status')
    list_filter = ('status',)
    search_fields = ('id', 'automobilis__klientas', 'automobilis__valstybinis_nr')

    class UzsakymoeilInline(admin.TabularInline):
        model = Uzsakymoeil
        extra = 1

    inlines = [UzsakymoeilInline]


@admin.register(Automobilis)
class AutomobilisAdmin(admin.ModelAdmin):
    list_display = ('valstybinis_nr', 'klientas', 'modelis', 'vin')
    list_filter = ('modelis__modelis', 'klientas')
    search_fields = ('valstybinis_nr', 'vin')


@admin.register(Paslauga)
class PaslaugaAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas', 'kaina')
    search_fields = ('pavadinimas',)


admin.site.register(Modelis)
admin.site.register(Uzsakymoeil)
# Register your models here.
