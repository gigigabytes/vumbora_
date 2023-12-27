// Get start
const one = document.getElementById('first')
const two = document.getElementById('second')
const three = document.getElementById('third')
const four = document.getElementById('fourth')
const five = document.getElementById('fifth')

const form = document.getElementById('f-avaliar')
const confirmbox = document.getElementById('confirm-box')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
const url = document.body.getAttribute('data-url')
const comentarioInput = document.getElementById('id_comentario');  // Substitua 'id_do_seu_campo_de_comentario' pelo ID correto


const handleStarSelect = (size) =>{
    const children = form.children
    
    for(let i=0; i < children.length; i++){
        if(i <= size){
            children[i].classList.add('checked')
        }else{
            children[i].classList.remove('checked')
        }
    }
} 
handleStarSelect(1)
const handleSelect = (selection) => {
    switch(selection){ 
        case 'first' :{
            // one.classList.add('checked')
            // two.classList.remove('checked')
            // three.classList.remove('checked')
            // four.classList.remove('checked')
            // five.classList.remove('checked')
            handleStarSelect(1)
            break;
        }
        case 'second':{
            handleStarSelect(2)
            break
        }
        case 'third':{
            handleStarSelect(3)
            break;
        }
        case 'fourth':{
            handleStarSelect(4)
            break;
        }
        case 'fifth':{
            handleStarSelect(5)
            break;
        }

}} 

const getnumericValue = (stringValue) => {
    let numericValue;
    if(stringValue === 'first'){
        numericValue = 1}
    else if (stringValue === 'second'){
        numericValue = 2}
    else if (stringValue === 'third'){
        numericValue = 3}
    else if (stringValue === 'fourth'){
        numericValue = 4}
    else if (stringValue === 'fifth'){
        numericValue = 5}
    else {
        numericValue = 0}
    
    return numericValue
}
let valNum;
let usuario =2

if (one){
    const arr = [one,two,three,four,five]
    arr.forEach(item => item.addEventListener('mouseover',(event)=> {
        handleSelect(event.target.id)
    }))

    arr.forEach(item => item.addEventListener('click',(event)=> {
        const val = event.target.id
        form.addEventListener('submit', e =>{
            e.preventDefault()
            const id = e.target.id
            
        })

        $.ajax({
            type:'POST',
            url: url,
            data:{
                'csrfmiddlewaretoken': csrf[0].value,
                'nota': getnumericValue(val),
                'usuario': usuario,
            },
            success: function(response){
                alert('Obrigado por avaliar', response);
                console.log(response)
            
                setTimeout(function(){
                    window.location.href = url
                }, 1000)    
            },
        })
}))
}

// Enviar comentário
document.getElementById('button-enviar').addEventListener('click', function(){
    const comentario = comentarioInput.value
    
    $.ajax({
        type:'POST',
        url: url,
        data:{
            'csrfmiddlewaretoken': csrf[0].value,
            'comentario': comentario,
            'usuario': usuario,
        },
        success: function(response){
            alert('Obrigado por comentar', response);
            console.log(response)
        
            setTimeout(function(){
                window.location.href = url
            }, 1000)    
        },
    })
}

)

