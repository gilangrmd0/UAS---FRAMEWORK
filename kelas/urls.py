from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from dashboard.views import dashboard, cart, category, hapus_brg, ubah_brg, hapus_minum, ubah_minum, tambah_minum, wish, tambah_barang, tampil_minum, Barang_View, tampil_promo, tambah_promo, ubah_promo, hapus_promo
from dashboard.views import *

# def coba1(request):
#     return HttpResponse('Selamat Datang !')
 
def coba2(request):
    title= "Home"
    konteks = {
        'titlenya': title,
    }
    return render(request, 'home.html', {'navbar':'home'})

def cart(request):
    title= "Cart"
    konteks = {
        'titlenya': title,
    }
    return render(request, 'cart.html', {'navbar':'cart'})

def wish(request):
    title= "Wish"
    konteks = {
        'titlenya': title,
    }
    return render(request, 'wish.html', {'navbar':'wish'})



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', coba1),
    path('', coba2),
    path('dashboard/', dashboard),
    path('category/', category),
    path('cart/', cart),
    path('wish/', wish),
    path('tambah_barang/', tambah_barang),
    path('tambah_minum/', tambah_minum),
    path('tambah_promo', tambah_promo),
    path('Vbrg/', Barang_View),
    path('tampil_minum/', tampil_minum),
    path('tampil_promo/', tampil_promo),
    path('ubahbrg/<int:id_barang>',ubah_brg, name='ubah_brg'),
    path('hapusbrg/<int:id_barang>',hapus_brg, name='hapus_brg'),
    path('ubahminum/<int:id_minuman>',ubah_minum, name='ubah_minum'),
    path('hapusminum/<int:id_minuman>',hapus_minum, name='hapus_minum'),
    path('ubahpromo/<int:id_promo>', ubah_promo, name='ubah_promo'),
    path('hapuspromo/<int:id_promo>', hapus_promo, name='hapus_promo'),


]
