function modificarFiltros() {
    let filtro = document.getElementById("filtro-body")
    filtro.classList.toggle("filtro-body-hidden");
    
    let flag = document.getElementById("flag-rotate")
    flag.classList.toggle("flag-filtros-rotate");
}

$(document).ready(function() {
    $('#form').on('submit', function(e) {
        e.preventDefault();
        
        const erros = validarForm();

        if (erros.length > 0) {
            $('#erros').empty();
            
            erros.forEach(function(error) {
                $('#erros').append('<div class="alert alert-danger">' + error + '</div>');
            });
        } 
        else {
            this.submit();
        }
    });
});

function validarForm() {
    const erros = [];

    const valor = $('#id_valor').val();
    if (valor <= 0) {
        erros.push('O valor precisa ser um valor positivo');
    }

    const nome = $('#id_nome').val();
    if (!String(nome).trim()) {
        erros.push('O campo nome precisa ser preenchido');
    }

    const descricao = $('#id_descricao').val();
    if (!String(descricao).trim()) {
        erros.push('O campo descricao precisa ser preenchido');
    }
    
    return erros;
}