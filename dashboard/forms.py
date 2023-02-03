from django.forms import ModelForm
from dashboard.models import Barang, minuman, promo
from django import forms

class FormBarang(ModelForm):
    class Meta:
        model=Barang
        fields='__all__'

        widgets = {
            'kodebrg': forms.TextInput({'class':'form-control'}),
            'nama': forms.TextInput({'class':'form-control'}),
            'stok': forms.NumberInput({'class':'form-control'}),
            'harga': forms.NumberInput({'class':'form-control'}),
            'link_gbr': forms.TextInput({'class':'form-control'}),
            'jenis_id': forms.Select({'class':'form-control'}),
        }

class Formminuman(ModelForm):
    class Meta:
        model=minuman
        fields='__all__'

        widgets = {
            'kodeminuman': forms.TextInput({'class':'form-control'}),
            'nama': forms.TextInput({'class':'form-control'}),
            'stok': forms.NumberInput({'class':'form-control'}),
            'harga': forms.NumberInput({'class':'form-control'}),
            'link_gbr': forms.TextInput({'class':'form-control'}),
            'jeniss_id': forms.Select({'class':'form-control'}),
        }

class Formpromo(ModelForm):
    class Meta:
        model=promo
        fields='__all__'

        widgets = {
            'kodepromo': forms.TextInput({'class':'form-control'}),
            'nama': forms.TextInput({'class':'form-control'}),
            'stok': forms.NumberInput({'class':'form-control'}),
            'harga': forms.NumberInput({'class':'form-control'}),
            'link_gbr': forms.TextInput({'class':'form-control'}),
            'jenisss_id': forms.Select({'class':'form-control'}),
        }
