const modalCadastro = new bootstrap.Modal(document.getElementById('modalcadastro'));

function alterar(id) {
    fetch("http://127.0.0.1:3333/cliente/" + id)
    .then(response => response.json())
    .then(dados => {
        document.getElementById('id').value = dados.id;
        document.getElementById('nome').value = dados.nome;
        document.getElementById('email').value = dados.email;
        document.getElementById('telefone').value = dados.telefone;
        document.getElementById('endereco').value = dados.endereco;
        modalCadastro.show();
    });
}

function excluir(id) {
    fetch("http://127.0.0.1:3333/cliente/" + id, {
        method: "DELETE",
    }).then(function () {
        listar();
    });
}

function salvar() {
    let id = document.getElementById('id').value;
    let nome = document.getElementById('nome').value;
    let email = document.getElementById('email').value;
    let telefone = document.getElementById('telefone').value;
    let endereco = document.getElementById('endereco').value;

    let cliente = { nome, email, telefone, endereco };

    const url = id 
        ? "http://127.0.0.1:3333/cliente/" + id
        : "http://127.0.0.1:3333/cliente";

    const metodo = id ? "PUT" : "POST";

    fetch(url, {
        method: metodo,
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(cliente)
    }).then(() => {
        listar();
        modalCadastro.hide();
    });
}

function novo() {
    document.getElementById('id').value = '';
    document.getElementById('nome').value = '';
    document.getElementById('email').value = '';
    document.getElementById('telefone').value = '';
    document.getElementById('endereco').value = '';
    modalCadastro.show();
}

function listar() {
    const lista = document.getElementById('lista');
    lista.innerHTML = "<tr><td colspan='6'>Carregando...</td></tr>";

    fetch('http://127.0.0.1:3333/cliente')
     .then(response => response.json())
     .then(dados => mostrar(dados));
}

function mostrar(dados){
    const lista = document.getElementById('lista');
    lista.innerHTML = "";
    for (let c of dados) {
        lista.innerHTML += "<tr>"
                + "<td>" + c.id + "</td>"
                + "<td>" + c.nome + "</td>"
                + "<td>" + c.email + "</td>"
                + "<td>" + c.telefone + "</td>"
                + "<td>" + c.endereco + "</td>"
                + "<td>" + new Date(c.data_cadastro).toLocaleString() + "</td>"
                + "<td>"
                + "<button type='button' class='btn btn-primary' onclick='alterar(" + c.id + ")'>Editar</button> "
                + "<button type='button' class='btn btn-danger' onclick='excluir(" + c.id + ")'>Excluir</button>"
                + "</td>"
                + "</tr>";
    }
}