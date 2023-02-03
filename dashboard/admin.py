from django.contrib import admin

from .models import Barang, Jenis
from .models import minuman,Jeniss
from .models import promo,Jenisss

class kolomBarang(admin.ModelAdmin):
    list_display = ['kodebrg','nama','stok','harga','jenis_id']
    search_fields = ['kodebrg','nama']
    list_filter = ('jenis_id',)
    list_per_page = 3



admin.site.register(Barang,kolomBarang)
admin.site.register(Jenis)

class kolomminuman(admin.ModelAdmin):
    list_display = ['kodeminuman','nama','stok','harga','jeniss_id']
    search_fields = ['kodeminuman','nama']
    list_filter = ('jeniss_id',)
    list_per_page = 3

admin.site.register(minuman,kolomminuman)
admin.site.register(Jeniss)

class kolompromo(admin.ModelAdmin):
    list_display = ['kodepromo','nama','stok','harga','jenisss_id']
    search_fields = ['kodepromo','nama']
    list_filter = ('jenisss_id',)
    list_per_page = 3

admin.site.register(promo,kolompromo)
admin.site.register(Jenisss)