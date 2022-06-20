import Produto from "./Produto.js";

function GetProdutosLiterais() {
    return [{
        id: 1,
        nome: "Bisturi Descartável Health Med",
        descricao: `Cabo em poliestireno de alto impacto. 
            
            Capa: Polietileno de alta densidade. 
            
            Fabricada em aço carbono. 
            
            Embalado em papel grau cirúrgico. 
            
            Esterilizadas por Raios Gama.
            
            Contém: 01 Bisturi Descartável nº 15.`,
        images: [
            "./images/bisturi1.jpg",
            "./images/bisturi2.jpg"
        ],
        categorias: [
            "Cuidados com a pele",
            "Cortar pele",
            "Equipamento Médico"
        ],
        preco: 87816,
        marca: "Health Med",
        disponivelParaLocalidades: [
            "29755971",
            "49540942",
            "59050889",
            "42103780",
            "76243820",
            "78841156",
            "10931969",
            "42823125",
            "78369553",
            "43155022"
        ]
    },
    {
        id: 2,
        nome: "Tesoura Cirúrgica Romba",
        descricao: `Código: 0311

                REG. MS: 10304850053.

                Utilizado para secção de fios e outros materiais.

                Ponta romba.

                Material: Produto Confeccionado em Aço Inoxidável Cirúrgico (AISI-420).

                Embalagem: Plástica individual, constando os dados de identificação, procedência e rastreabilidade.

                Marca: ABC.`,
        images: [
            "./images/tesoura1.jpg",
            "./images/tesoura2.jpg"
        ],
        categorias: [
            "Cuidados com o cabelo",
            "Cortar cabelo e pele",
            "Equipamento Médico"
        ],
        preco: 32530,
        marca: "Abc",
        disponivelParaLocalidades: [
            "33145300",
            "59151902",
            "68513227",
            "54580060",
            "72927830",
            "90440020",
            "29755971",
            "49540942",
        ]
    }, {
        id: 3,
        nome: "Pinça Anatômica Dente De Rato Abc ",
        descricao: `Código: 0177

                REG. MS: 10304850059.

                Material: Produto Confeccionado em Aço Inoxidável Cirúrgico (AISI-420).

                Anatômica.

                Possui dentes na extremidade.

                Embalagem: Plástica individual, constando os dados de identificação, procedência e rastreabilidade.

                Marca: ABC.`,
        images: ["./images/pinca1.jpg"],
        categorias: [
            "Cuidados com as unhas",
            "Pinças unha e pele",
            "Equipamento Médico"
        ],
        preco: 61979,
        marca: "Abc",
        disponivelParaLocalidades: [
            "33145300",
            "59151902",
            "68513227",
            "54580060",
        ]
    }, {
        id: 4,
        nome: "Cinta para Bolsa de Colostomia 3 Bandas",
        descricao: `A cinta para bolsa de colostomia com 3 elásticos e velcro Flambé é fabricada em elástico e tecido semi-elástico e semi-rígido, para auxiliar o uso da bolsa de colostomia de forma segura e confortável, facilitando a realização das tarefas diárias.

                Pode ser utilizada em diferentes situações e, para todas elas, prioriza sempre o conforto e bem-estar.

                Características
                - Suporte para bolsa de colostomia descartável;
                - Forração interna com tecido ultra macio;
                - Fechamento com velcro;
                - Uso bilateral;
                - Unissex.

                Além disso, a cinta para bolsa de colostomia com 3 elásticos e velcro Flambé possui fecho aderente, que permite o ajuste da compressão conforme a necessidade individual, garantindo mais conforto durante o uso.

                Tamanho G/GG:

                Comprimento da faixa: 125cm;
                Altura da faixa: 21cm.
                Cor: Bege.`,
        images: [
            "./images/bolsa-colo1.jpg",
            "./images/bolsa-colo2.jpg"
        ],
        categorias: [
            "Cuidados com o intestino",
            "Bolsa de cocô",
            "Equipamento Médico"
        ],
        preco: 77571,
        marca: "Flambé ",
        disponivelParaLocalidades: [
            "72927830",
            "90440020",
            "29755971",
            "49540942",
        ]
    }
    ]
}

const produtosLiterais = GetProdutosLiterais();

const produtosObjetos = [];

for (const produto of produtosLiterais) {
    produtosObjetos.push(
        new Produto(
            produto.id,
            produto.nome,
            produto.descricao,
            produto.images,
            produto.categorias,
            produto.preco,
            produto.marca,
            produto.disponivelParaLocalidades
        )
    );
};

const cardGroupElements = produtosObjetos.map(produto => {

    const carrousel = produto.Imagens.map((image, index) => {
        return `
            <div class="carousel-item ${index == 0 ? "active" : ""}">
                <div class="d-flex justify-content-center align-items-center" style="height: 300px;">
                    <img src="${image}" class="d-block w-50" alt="${produto.nome}" >
                </div>
            </div>
        `;
    });

    return `
        <div class="col mb-4">
            <div class="card">

                <div id="carouselControls${produto.Id}" class="carousel slide" data-ride="carousel">
                    <div class="carousel-inner">
                        ${carrousel.join("")}
                    </div>
                    <button class="carousel-control-prev" type="button" data-target="#carouselControls${produto.Id}" data-slide="prev">
                        <span class="carousel-control-prev-icon" style="filter: invert(100%);" "aria-hidden="true"></span>
                        <span class="sr-only">Previous</span>
                    </button>
                    <button class="carousel-control-next" type="button" data-target="#carouselControls${produto.Id}" data-slide="next">
                        <span class="carousel-control-next-icon" style="filter: invert(100%);" aria-hidden="true"></span>
                        <span class="sr-only">Next</span>
                    </button>
                </div>                    

                <div class="card-body">
                    <h5 class="card-title m-0">${produto.Nome}</h5>
                    <small class="card-text">Fabricante: ${produto.Marca}</small>
                    <p class="card-text mt-2">${produto.PrecoEmReais()}</p>

                    <p><a data-toggle="collapse" href="#collapse${produto.Id}" role="button" aria-expanded="false" aria-controls="collapse${produto.Id}">
                        Exibir descrição...
                    </a></p>
                    <div class="collapse" id="collapse${produto.Id}">
                        <div class="card card-body">
                        ${produto.Descricao}
                        </div>
                    </div>

                    <p class="card-text"></p>                        
                    ${produto.Categorias.map(categoria => `<span class="badge badge-light">${categoria}</span>`).join('')}                        
                    <p class="card-text mt-2">Disponível para as seguintes localidades:</p>
                    ${produto.DisponivelParaCeps().map(ceps => `<span class="badge badge-info">${ceps}</span>`).join('')}
                </div>
            </div>
        </div>
    `;
});

const div = `
    <div class="container">
        <div class="row row-cols-1 row-cols-md-2">
            ${cardGroupElements.join("")}
        </div>
    </div>
`;

$("body").append(div);
