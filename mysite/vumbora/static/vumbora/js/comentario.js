// Função para pegar o valor do input e colocar no comentário

// const datanota = document.querySelectorAll('.coment-section');
// datanota.forEach((section)=>{
//     const nota = section.getAttribute('data-nota');
//     if (nota === '1'){
//         const nota1 = section.querySelector('#nota1');
//         nota1.checked = true;
//     }
// })

// comentario.js

$(document).ready(function() {
    // Access the data-nota attribute for each .coment-section
    $('.coment-section').each(function() {
        var nota = $(this).data('nota');
        var avaliacaoId = $(this).find('.nota-btn').attr('id').split('_')[1];
        
        // Convert nota to a number before comparing
        var notaValue = parseInt(nota, 10);

        // Compare nota to values like 1 or 5
        switch(notaValue){
            case 1:
                $('#um_' + avaliacaoId).addClass('checked');
                break;
            case 2:
                $('#um_' + avaliacaoId).addClass('checked');
                $('#dois_' + avaliacaoId).addClass('checked');
                break;
            case 3:
                $('#um_' + avaliacaoId).addClass('checked');
                $('#dois_' + avaliacaoId).addClass('checked');
                $('#tres_' + avaliacaoId).addClass('checked');
                break;
            case 4:
                $('#um_' + avaliacaoId).addClass('checked');
                $('#dois_' + avaliacaoId).addClass('checked');
                $('#tres_' + avaliacaoId).addClass('checked');
                $('#quatro_' + avaliacaoId).addClass('checked');
                break;
            case 5:
                $('#um_' + avaliacaoId).addClass('checked');
                $('#dois_' + avaliacaoId).addClass('checked');
                $('#tres_' + avaliacaoId).addClass('checked');
                $('#quatro_' + avaliacaoId).addClass('checked');
                $('#cinco_' + avaliacaoId).addClass('checked');
                break;

        }
    });
});
