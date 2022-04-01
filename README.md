# cs-medmais
Site em HTML + CSS + JS da disciplina TCC00226 - DESENVOLVIMENTO WEB da Universidade Federal Fluminense

# Compilando o projeto

Neste trabalho foi utilizado um pré-processador (GULP), que serve para automatizar algumas tarefas no desenvolvimento web, e o motivo do gulp estar neste projeto é utilizar os imports de arquivos HTML dentro de outros arquivos HTML, deste forma, poderemos componentizar e reutilizar grante parte dos códigos sem precisar repeti-los, fazendo com que o projeto fique mais manutenível e uma modificação seja em um arquivo seja propagada para onde este arquivo estiver incluído.

### Como utilizar?
1 - Instale o Node na sua máquina
2 - Instale o `gulp cli` no node de forma global com o seguinte comando
`npm install --global gulp-cli`
3 - Na raiz do projeto execute os comandos
`npm i` -> para instalar as dependências do gulp
`gulp` -> para compilar o projeto
4 - Abra a pasta dist e o html pós processado estará lá com o projeto

