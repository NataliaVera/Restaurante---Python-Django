from django import forms

class FormularioRegistroPlatos(forms.Form):

    nombrePlato= forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=50,
        required= True
    )
    descripcionPlato=forms.CharField(
        widget=forms.Textarea(attrs={"class":"form-control mb-3"}),
        max_length=200,
        required= True
    )
    fotoPlato=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=200,
        required= True
    )
    precioPlato=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required= True
    )
    tipoPlato=forms.ChoiceField(
        widget=forms.Select(attrs={"class":"form-conrol mb-3"})
    )

