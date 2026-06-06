from django import forms
from .models import PontoTuristico

class PontoTuristicoForm(forms.ModelForm):
    class Meta:
        model = PontoTuristico

        fields = [
            "nome", "descricao", "categoria", "estado", 
            "municipio", "bairro",
            "logradouro", "numero", "complemento", "cep", "ativo","latitude", "longitude"
        ]

        labels = {
            "nome": "Nome",
            "descricao": "Descrição",
            "categoria": "Categoria",
            "estado": "Estado",
            "municipio": "Município",
            "bairro": "Bairro",
            "logradouro": "Logradouro",
            "numero": "Número",
            "complemento": "Complemento",
            "cep": "CEP",
            "ativo": "Ativo",
        }

        widgets = {
            "nome": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Nome do ponto turístico"
            }),

            "descricao": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Descrição do local"
            }),

            "categoria": forms.Select(attrs={
                "class": "form-select"
            }),

            "estado": forms.Select(attrs={
                "class": "form-select"
            }),

            "municipio": forms.Select(attrs={
                "class": "form-select"
            }),

            "bairro": forms.Select(attrs={
                "class": "form-select"
            }),

            "logradouro": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Rua / Avenida"
            }),

            "numero": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Número"
            }),

            "complemento": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Complemento"
            }),

            "cep": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "00000-000"
            }),

            "ativo": forms.CheckboxInput(attrs={
                "class": "form-check-input"
            }),
        }