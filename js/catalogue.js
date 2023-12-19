
const addToCartButtons = document.querySelectorAll('button');

function addToCartClicked(event){
    event.preventDefault() ; 
    let catalogueDetails = localStorage.getItem("catalogueDetails") ;
    const parentTR = event.target.closest('tr') ; 
    const tdElements = parentTR.querySelectorAll('td') ; 
    if(parentTR){
        alert(tdElements[0].querySelector('img').src) ; 
        alert(tdElements[1].textContent) ; 
        alert(tdElements[2].textContent) ; 
        if(catalogueDetails == null){
            let catalogueJSON = [] ; 
            catalogueJSON.push({img : tdElements[0].querySelector('img').src , Name : tdElements[1].textContent ,cost : tdElements[2].textContent , qty: 1}) ; 
            localStorage.setItem("catalogueDetails",JSON.stringify(catalogueJSON)) ;
            // alert("Password Saved") ; 
        }
        else {
            let catalogueJSON = JSON.parse(catalogueDetails) ; 
            for(let i=0 ; i<catalogueJSON.length ; i++){
                let row = catalogueJSON[i] ; 
                if(row.Name === tdElements[1].textContent) {
                    row.qty += 1 ; 
                    localStorage.setItem("catalogueDetails",JSON.stringify(catalogueJSON)) ;
                    return ; 
                }
            }
            catalogueJSON.push({img : tdElements[0].querySelector('img').src , Name : tdElements[1].textContent ,cost : tdElements[2].textContent , qty : 1}) ; 
            localStorage.setItem("catalogueDetails",JSON.stringify(catalogueJSON)) ;
        }
    }
}
addToCartButtons.forEach(button => {
    button.addEventListener('click',addToCartClicked) ; 
}) ; 