$(document).ready( function () {
    $('#tabela').DataTable({
      searching: true,
      ordering: true,
      paging: true,
      language: {
        url:"https://cdn.datatables.net/plug-ins/1.11.3/i18n/pt_br.json"
      }      
    });
} );