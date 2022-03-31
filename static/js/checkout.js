

var sendCheckout = document.getElementsByClassName('send-to-payment-data');
for (var i=0; i<sendCheckout.length; i++){
    sendCheckout[i].addEventListener('click', function(){
        var total_pp = total_total_final();
        var urll = this.dataset.url
        
        
        open_checkout(total_pp, urll);
    })
}


function open_checkout(total_pp,urll){
    console.log('Send data of payment')
    var url = 'save_total_payment/'

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'total_pay':total_pp})
    }).then(res => res.json())
    .catch(error => console.error('Error:', error))
    .then(response => {
      console.log("Success: ", response)
      if (response == "Item was added"){
        document.location.href = urll;
    }
    }
      );

    
    

}