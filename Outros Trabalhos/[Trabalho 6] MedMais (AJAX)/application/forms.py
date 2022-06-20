from django import forms
from django.core.exceptions import ValidationError

from domain.models import Parceiro, Produto
from medmais import settings


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

class QuantidadeDeProdutoForm(forms.Form):
    produto_id = forms.CharField(widget=forms.HiddenInput)
    quantidade = forms.IntegerField(
        min_value=0,
        max_value=99,
        widget=forms.TextInput(attrs={'class': 'form-control text-center quantidade',
            'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57)'
        }),
        required=True
    )

class ProdutoForm(forms.ModelForm):
    quantidade = forms.IntegerField(
        min_value=0,
        max_value=99,
        widget=forms.TextInput(attrs={'class': 'form-control',
            'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57)'
        }),
        required=True
    )

    class Meta:
        model = Produto
        fields = ('nome', 'descricao', 'parceiro', 'data_cadastro', 'preco', 'disponivel')
        localized_fields = ('preco',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].error_messages={'required': 'Campo obrigatório.',
                                            'unique': 'Nome de produto duplicado.'}
        self.fields['nome'].widget.attrs.update({'class': 'form-control'})

        self.fields['descricao'].error_messages={'required': 'Campo obrigatório'}
        self.fields['descricao'].widget.attrs.update({'class': 'form-control'})

        self.fields['parceiro'].error_messages={'required': 'Campo obrigatório'}
        self.fields['parceiro'].queryset=Parceiro.objects.all().order_by('nome')
        self.fields['parceiro'].empty_label='--- Selecione um Parceiro ---'
        self.fields['parceiro'].widget.attrs.update({'class': 'form-control'})

        self.fields['data_cadastro'].error_messages={'required': 'Campo obrigatório',
                                                     'invalid': 'Data inválida'}
        self.fields['data_cadastro'].input_formats=settings.DATE_INPUT_FORMATS
        self.fields['data_cadastro'].widget.attrs.update({'class': 'form-control'})

        self.fields['preco'].min_value=0
        self.fields['preco'].error_messages={'required': 'Campo obrigatório.',
                                             'invalid': 'Valor inválido.'}
        self.fields['preco'].widget.attrs.update({
            'class': 'form-control',
            'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57)'
        })

        self.fields['disponivel'].widget.attrs.update({'class': 'form-control'})