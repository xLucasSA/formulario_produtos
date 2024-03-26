function modificarFiltros() {
    let filtro = document.getElementById("filtro-body")
    filtro.classList.toggle("filtro-body-hidden");
    
    let flag = document.getElementById("flag-rotate")
    flag.classList.toggle("flag-filtros-rotate");
}