// var option = document.getElementsByTagName("option")[0];
// var size = option.dataset.target;

var sizeExists = document.getElementById("sizes");





var size = null
if (sizeExists != null) {
    document.getElementById('sizes').addEventListener('change', function() {
        //console.log('You selected: ', this.value);
        size = this.value;
    });
}
var updateBtns = document.getElementsByClassName('update-cart');

for(var i =0; i<updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product;
        var action = this.dataset.action;
        var category = this.dataset.type;
        var temp_size = this.dataset.size;
        
        if (temp_size != null){
            size = temp_size;
        }
        console.log('product id: ', productId, 'action: ',action, 'Type: ',category);
        if(size != null){
            console.log('product id: ', productId, 'action: ',action,"Size", size, 'Type: ',category);
        }
       
        console.log('User: ', user);
        if (user === 'AnonymousUser'){
          console.log('Not logged in');
        }
        else{
            updateUserOrder(productId, action, category);
        }  
        
       
    })
}

function updateUserOrder(productId, action, category){
    console.log('Send data');

    var url= 'update_item/';

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action':action, 'category':category,'size':size})
    }).then(res => res.json())
    .catch(error => console.error('Error:', error))
    .then(response => {
        if (response == 'Item was not added'){
            alert("Select a size");
            console.log("Success: ", response);
        }
        else{
            console.log("Success: ", response);
        }
    });

   
    
}