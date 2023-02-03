from django.shortcuts import render, redirect
from dashboard.forms import FormBarang, Formminuman, Formpromo
from dashboard.models import Barang, minuman, promo
from django.contrib import messages
from dashboard.views import *


def hapus_promo(request, id_promo):
    promos=promo.objects.filter(id=id_promo)
    promos.delete()
    messages.success(request, "Data Terhapus")
    return redirect('/tampil_promo')

def ubah_promo(request, id_promo):
    promos=promo.objects.get(id=id_promo)
    if request.POST:
        form=Formpromo(request.POST, instance=promos)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil diubah")
            return redirect('ubah_promo', id_promo=id_promo)
    else:
        form=Formpromo(instance=promos)
        konteks = {
            'form' : form,
            'promos' : promos
        }
    return render(request,'ubah_promo.html', konteks)

def tampil_promo(request):
    promos=promo.objects.all()

def tambah_promo(request):
    if request.POST:
        form = Formpromo(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Ditambahkan")
            form = Formpromo()
            konteks = {
                'form' : form,
            }
            return render(request, 'tambah_promo.html', konteks)
    else:
        form=Formpromo()
        konteks = {
            'form' : form,
        }
    return render(request, 'tambah_promo.html', konteks)



##minum
def hapus_minum(request, id_minuman):
    minums=minuman.objects.filter(id=id_minuman)
    minums.delete()
    messages.success(request, "Data Terhapus")
    return redirect('/tampil_minum')

def ubah_minum(request, id_minuman):
    minums=minuman.objects.get(id=id_minuman)
    if request.POST:
        form=Formminuman(request.POST, instance=minums)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil diubah")
            return redirect('ubah_minum', id_minuman=id_minuman)
    else:
        form=Formminuman(instance=minums)
        konteks = {
            'form' : form,
            'minums' : minums
        }
    return render(request,'ubah_minum.html', konteks)

def tampil_minum(request):
    minums=minuman.objects.all()

def tambah_minum(request):
    if request.POST:
        form = Formminuman(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Ditambahkan")
            form = Formminuman()
            konteks = {
                'form' : form,
            }
            return render(request, 'tambah_minum.html', konteks)
    else:
        form=Formminuman()
        konteks = {
            'form' : form,
        }
    return render(request, 'tambah_minum.html', konteks)

##barang
def hapus_brg(request, id_barang):
    barangs=Barang.objects.filter(id=id_barang)
    barangs.delete()
    messages.success(request, "Data Terhapus")
    return redirect('/Vbrg')

def ubah_brg(request, id_barang):
    barangs=Barang.objects.get(id=id_barang)
    if request.POST:
        form=FormBarang(request.POST, instance=barangs)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil diubah")
            return redirect('ubah_brg', id_barang=id_barang)
    else:
        form=FormBarang(instance=barangs)
        konteks = {
            'form' : form,
            'barangs' : barangs
        }
    return render(request,'ubah_brg.html', konteks)

def Barang_View(request):
    barangs=Barang.objects.all()

def tambah_barang(request):
    if request.POST:
        form = FormBarang(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Ditambahkan")
            form = FormBarang()
            konteks = {
                'form' : form,
            }
            return render(request, 'tambah_barang.html', konteks)
    else:
        form=FormBarang()
        konteks = {
            'form' : form,
        }
    return render(request, 'tambah_barang.html', konteks)

def dashboard(request):
    title= "Dashboard"
    konteks = {
        'titlenya': title,
    }
    return render(request, 'dashboard.html', konteks)

def Barang_View(request):
    barangs = Barang.objects.all()

    konteks = {
        'barangs':barangs,
    }

    return render (request, 'tampil_brg.html', konteks)

def tampil_minum(request):
    minums = minuman.objects.all()

    konteks = {
        'minums':minums,
    }

    return render (request, 'tampil_minum.html', konteks)

def tampil_promo(request):
    promos = promo.objects.all()

    konteks = {
        'promos':promos,
    }

    return render (request, 'tampil_promo.html', konteks)

def cart(request):
    title= "Cart"
    konteks = {
        'titlenya': title,
    }
    return render(request, 'cart.html', konteks)


def category(request):
    title= "Category"
    konteks = {
        'titlenya': title,
    }
    return render(request, 'category.html', konteks)

def wish(request):
    title= "Wish"
    konteks = {
        'titlenya': title,
    }
    return render(request, 'wish.html', konteks)
    