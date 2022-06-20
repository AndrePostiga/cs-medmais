import locale

from django.db import models

from domain.helpers import formata_preco_em_centavos


class Parceiro(models.Model):
    cnpj = models.CharField(max_length=14, db_index=True, unique=True, blank=False)
    nome = models.CharField(max_length=100, db_index=False, blank=False)
    endereco = models.CharField(max_length=300, db_index=False, blank=False)
    telefone = models.CharField(max_length=11, db_index=False, blank=False)
    data_cadastro = models.DateField()
    data_atualizacao = models.DateField(blank=True)

    class Meta:
        db_table = 'parceiros'

    def __str__(self):
        return self.nome

    def get_cnpj(self):
        return f'{self.cnpj[0:2]}.{self.cnpj[2:5]}.{self.cnpj[5:8]}/{self.cnpj[8:12]}-{self.cnpj[12:14]}'

    def get_telefone(self):
        return f'({self.telefone[0:2]}) {self.telefone[2:7]}-{self.telefone[7:11]}'

class Produto(models.Model):
    parceiro = models.ForeignKey(Parceiro, related_name='produtos', on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=100, db_index=True, unique=False)
    descricao = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    preco = models.IntegerField(default=0)
    data_cadastro = models.DateField()
    disponivel = models.BooleanField(default=False)

    class Meta:
        db_table = 'produto'

    def __str__(self):
        return self.nome

    def get_disponivel(self):
        return "Sim" if self.disponivel else "Não"

    def get_preco(self):
        return formata_preco_em_centavos(self.preco)

class Cliente(models.Model):
    nome = models.CharField(max_length=100, db_index=True, unique=True)
    imagem = models.CharField(max_length=50, blank=True)

    class Meta:
        db_table = 'cliente'

    def __str__(self):
        return self.nome


class Objetivo(models.Model):
    nome = models.CharField(max_length=100, db_index=True, unique=True)
    texto = models.TextField(max_length=1000, db_index=False, blank=True)

    class Meta:
        db_table = 'objetivo'

    def __str__(self):
        return self.nome


class CardContato(models.Model):
    titulo = models.CharField(max_length=100, db_index=True, unique=True)
    imagem = models.CharField(max_length=50, blank=True)
    texto1 = models.CharField(max_length=255, db_index=False, blank=True)
    texto2 = models.CharField(max_length=255, db_index=False, blank=True)

    class Meta:
        db_table = 'card_contato'

    def __str__(self):
        return self.titulo


class CardServico(models.Model):
    titulo = models.CharField(max_length=100, db_index=True, unique=True)
    imagem = models.CharField(max_length=50, blank=True)
    miniatura = models.CharField(max_length=50, blank=True)
    ehNovo = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    texto = models.TextField(max_length=1000, db_index=False, blank=True)
    slug = models.SlugField(max_length=70)

    class Meta:
        db_table = 'card_servico'

    def __str__(self):
        return self.titulo
