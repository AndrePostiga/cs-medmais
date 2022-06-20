from django import forms
from django.core.exceptions import ValidationError

from domain.models import Parceiro


class ParceirosSearchForm(forms.Form):
    nome = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm form-nome rounded-0', 'max-lenght': '100', 'style': 'height: 40px;'}),
        required=False
    )

class ParceirosCadastroForm(forms.ModelForm):

    class Meta:
        model = Parceiro
        fields = ('cnpj', 'nome', 'endereco', 'telefone')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['cnpj'].error_messages={
            'required': 'Campo obrigatório',
            'unique': 'CNPJ duplicado'}
        self.fields['cnpj'].widget.attrs.update({
            'class': 'form-control',
            'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57)',
            'maxlength': '18'
        })

        self.fields['nome'].error_messages={'required': 'Campo obrigatório'}
        self.fields['nome'].widget.attrs.update({'class': 'form-control'})

        self.fields['endereco'].error_messages = {'required': 'Campo obrigatório'}
        self.fields['endereco'].widget.attrs.update({'class': 'form-control'})

        self.fields['telefone'].error_messages = {'required': 'Campo obrigatório', 'invalid': 'Campo inválido'}
        self.fields['telefone'].widget.attrs.update({
            'class': 'form-control',
            'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57)',
            'maxlength': '15'
        })

    def clean_cnpj(self):
        cnpj = self.cleaned_data['cnpj']

        lista_validacao_um = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        lista_validacao_dois = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

        # finding out the digits
        verificadores = cnpj[-2:]

        # verifying the lenght of the cnpj
        if len(cnpj) != 14:
            return False

        # calculating the first digit
        soma = 0
        id = 0
        for numero in cnpj:

            # to do not raise indexerrors
            try:
                lista_validacao_um[id]
            except:
                break

            soma += int(numero) * int(lista_validacao_um[id])
            id += 1

        soma = soma % 11
        if soma < 2:
            digito_um = 0
        else:
            digito_um = 11 - soma

        digito_um = str(digito_um)  # converting to string, for later comparison

        # calculating the second digit
        # suming the two lists
        soma = 0
        id = 0

        # suming the two lists
        for numero in cnpj:

            # to do not raise indexerrors
            try:
                lista_validacao_dois[id]
            except:
                break

            soma += int(numero) * int(lista_validacao_dois[id])
            id += 1

        # defining the digit
        soma = soma % 11
        if soma < 2:
            digito_dois = 0
        else:
            digito_dois = 11 - soma

        digito_dois = str(digito_dois)

        # returnig
        if bool(verificadores == digito_um + digito_dois):
            return cnpj

        raise ValidationError('CNPJ está inválido')
