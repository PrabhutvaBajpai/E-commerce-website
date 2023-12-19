// const cartTable = document.querySelector('.table') ;

// let catalogueDetails = localStorage.getItem("catalogueDetails") ; 
// let catalogueData = JSON.parse(catalogueDetails) || [] ;

// // To remove a book from Cart 

// const Del =(i) => { 
//     catalogueData.splice(i,1) ; 
//     localStorage.setItem('catalogueDetails'.JSON.stringify(catalogueData)) ; 
// }


// // To subtract the qty 

// const SUB = (i) => {
//     i = parseInt(i) ; // To convert i into Number . 
//     let quantity = catalogueData[i].qty ;
//     if(quantity === 1){
//         Del(i) ;
//         localStorage.setItem('catalogueDetails'.JSON.stringify(catalogueData)) ; 
//     }
//     else {
//         catalogueData[i].qty -= 1 ; 
//         localStorage.setItem('catalogueDetails',JSON.stringify(catalogueData)) ; 
//     }
    
// }

// // To add the qty 
 
// const ADD = (i) => {
//     i = parseInt(i) ; // To convert i into Number . 
//     catalogueData[i].qty += 1 ; 
//     localStorage.setItem('catalogueDetails',JSON.stringify(catalogueData)) ; 
// }


// if(catalogueData === 0){
//     alert("Nothing in Cart") ; 
// }
// else {
    
//     for(let i=0 ; i<catalogueData.length ; i++){
//         let row = catalogueData[i] ; 
//         let html = "" ; 
//         html += `
//         <tr>
//             <td> <img src="${row.img}" alt="Think and Grow Rich"></td>
//             <td>${row.Name}</td>
//             <td>${row.cost}</td>
//             <td>${row.qty}</td>
//             <td><button class = "minus" onClick = "SUB('${i}')">--</button> <button class="plus" onClick = "ADD('${i}')">+</button></td>
//         <tr>
//         `
//         cartTable.innerHTML += html ; 
//     }
// }
 
const cartTable = document.querySelector('.table');
let catalogueDetails = localStorage.getItem("catalogueDetails");
let catalogueData = JSON.parse(catalogueDetails) || [];

// To remove a book from Cart 
const Del = (i) => {
    catalogueData.splice(i, 1);
    localStorage.setItem('catalogueDetails', JSON.stringify(catalogueData));
}

// To subtract the qty 
const SUB = (i) => {
    i = parseInt(i); // Convert 'i' to a number
    let quantity = catalogueData[i].qty;
    if (quantity === 1) {
        Del(i);
    } else {
        catalogueData[i].qty -= 1;
        localStorage.setItem('catalogueDetails', JSON.stringify(catalogueData));
    }
}

// To add the qty 
const ADD = (i) => {
    i = parseInt(i); // Convert 'i' to a number
    catalogueData[i].qty += 1;
    localStorage.setItem('catalogueDetails', JSON.stringify(catalogueData));
}

if (!catalogueData || catalogueData.length === 0) {
    alert("Nothing in Cart");
} else {
    for (let i = 0; i < catalogueData.length; i++) {
        let row = catalogueData[i];
        let html = "";
        html += `
        <tr>
            <td> <img src="${row.img}" alt="Think and Grow Rich"></td>
            <td>${row.Name}</td>
            <td>${row.cost}</td>
            <td>${row.qty}</td>
            <td><button class="minus" onclick="SUB(${i})">--</button> <button class="plus" onclick="ADD(${i})">+</button></td>
        </tr>`;
        cartTable.innerHTML += html;
    }
}


