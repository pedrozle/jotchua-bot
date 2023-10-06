var listaDeTextos = [
    "animar",
    "bagunçar",
    "moderar",
    "divertir",
    "agitar",
    "colorir",
    "impulsionar",
];
var indice = 0;

// Função para atualizar o texto do parágrafo
function atualizarTexto() {
    var paragrafo = document.getElementById("changeText");
    paragrafo.innerHTML = listaDeTextos[indice];
    indice = (indice + 1) % listaDeTextos.length;
}

// Chama a função inicialmente
atualizarTexto();

// Define um intervalo para atualizar o texto a cada 5 segundos
setInterval(atualizarTexto, 2000);

let detalhesAtivo = "comandos-basicos";
const detalhesContainer = document.getElementById("detalhes-container");
const categoriaContainers = document.querySelectorAll(".categoria-container");

categoriaContainers.forEach((categoria) => {
    categoria.addEventListener("click", () => {
        // Obtém o valor do atributo data-categoria
        const categoriaSelecionada = categoria.getAttribute("data-categoria");

        // Agora você pode usar a categoriaSelecionada para carregar o conteúdo apropriado nos detalhes
        // Por exemplo, você pode ter um objeto ou uma função que mapeia categorias para conteúdo
        const conteudo = exibeDetalhes(categoriaSelecionada);
    });
});

function exibeDetalhes(categoria) {
    const conteudoAtivo = document.getElementById(detalhesAtivo);
    const conteudo = document.getElementById(categoria);
    detalhesAtivo = categoria;
    if (conteudoAtivo.classList.contains("exibe")) {
        conteudoAtivo.classList.remove("exibe");
    }

    conteudo.classList.add("exibe");
}
