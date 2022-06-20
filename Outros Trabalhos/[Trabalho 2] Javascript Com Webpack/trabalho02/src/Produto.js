export default class Produto {

    constructor(id, nome, descricao, imagens, categorias, precoEmCentavos, marca, disponivelParaLocalidades) {
        this.Id = id;
        this.Nome = nome;
        this.Descricao = descricao;
        this.Imagens = imagens;
        this.Categorias = categorias;
        this.Preco = precoEmCentavos;
        this.Marca = marca;
        this.DisponivelParaLocalidades = disponivelParaLocalidades;
    }

    PrecoEmReais() {
        this.Preco /= 100;
        return `R$ ${this.Preco.toFixed(2)}`.replace(".", ",");
    }

    DisponivelParaCeps() {
        return this.DisponivelParaLocalidades.map(cep => {
            return `${cep.substring(0, 5)}-${cep.substring(5)}`
        });
    }
}
