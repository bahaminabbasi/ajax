var updateBtns = document.getElementsByClassName('update-cart')


for (var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId: ', productId, 'action: ', action)

        updateUserOrder(productId, action)

        // console.log('USER: ', user)
        // if(user == 'AnonymousUser'){
        //     console.log('Not logged in')
        // }else{
        //     updateUserOrder(productId, action)
        // }
    })
}


function updateUserOrder(productId, action){
    console.log('User is logged in, sending data...')

    var url = '/cart/update_item/'
    $.ajax({
        url: url,
        method:'POST',
        data: {'productId': productId, 'action': action},
        success: function(data){
            console.log(data)
            location.reload()
            if (data['max_reached'] === 'yes'){

                window.alert("این تعداد موجود نمی باشد")

            }
        }
    });
}