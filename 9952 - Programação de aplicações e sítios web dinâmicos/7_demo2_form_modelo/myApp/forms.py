from django import forms

class AlunoForm(forms.Form):
    nome = forms.CharField(
        label='Nome',
        max_length=250,
        required=True,
        widget= forms.TextInput(attrs={'class': 'form-control'})
    )
    idade = forms.IntegerField(
        label='Idade',
        required=True,
        widget= forms.TextInput(attrs={'class': 'form-control'})
    )

    turma = forms.CharField(
        label='Turma',
        max_length=250,
        required=True,
        widget= forms.TextInput(attrs={'class': 'form-control'})
    )

