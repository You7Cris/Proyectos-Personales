var updateBts = document.getElementsByClassName("update-cart")

function updateCartBtn(){
    var productId = this.dataset.product
    var action = this.dataset.action
    console.log(productId, action)
    if (user === 'AnonymousUser' ) {
        console.log('Anonimo')
    } else {
        console.log('Esta registrado')
        updateUserOrder(productId, action)
    }
}

function updateUserOrder(productId, action){
    console.log("Sending info...", productId, action)
    var url = "/update-item/"

    fetch(url, {
        method : 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken
        },
        body:JSON.stringify(
            {
                'productId': productId,
                'action': action
            }
        )
    }).then((response) => {
        return response.json()
    }).then((data) =>{
        console.log('data', data)
        location.reload()
    })
}


for (let index = 0; index < updateBts.length; index++){
    // const element = array[index];

    updateBts[index].addEventListener('click', updateCartBtn)
}