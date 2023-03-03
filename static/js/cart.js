var updateBtns = document.getElementsByClassName('update-cart');

for( i = 0; i < updateBtns.length;  i++)
{
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'Action:', action)

        //Check User or Anonymous
        console.log('User', user)
        if(user == 'AnonymousUser')
        {
            console.log("User is not autheticated")
        }else{
            console.log("User is autheticated, sending data")

        }
    })
}