from django import forms

class FormularioRegistroEmpleados(forms.Form):

    CARGO=(
        (1, 'Mesero'),
        (2, 'Cocinero'),
        (3, 'Cajero'),
        (4, 'Admin')
    )

    nombreEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=50,
        required= True,
        label="Nombre"
    )
    apellidoEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=50,
        required= True,
        label="Apellido"
    )
    telefonoEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=50,
        required= True,
        label="Telefono"
    )
    cargoEmpleado=forms.ChoiceField(
        widget=forms.Select(attrs={"class":"form-control mb-3"}),
        label="Cargo",
        choices=CARGO
    )