document.querySelector('#SaveButton').addEventListener('click', (event) => {
    event.preventDefault();
    let Email = document.querySelector('#Email').value;
    let Password = document.querySelector('#Password').value;
    let loginDetails = localStorage.getItem("login");
    let loginData = JSON.parse(loginDetails);
    let flag = 0;
    
    if (!loginData || loginData.length === 0) {
        alert("No login data found");
        return;
    }

    for (let i = 0; i < loginData.length; i++) {
        let row = loginData[i];
        if (row.email === Email) {
            flag = 1;
            if (row.password === Password) {
                alert("Signed in successfully!");
                // Redirect to another page
                window.location.href = 'firstpage.html';
            } else {
                alert("Password is incorrect");
            }
            break;
        }
    }
    
    if (flag === 0) {
        alert("You are not logged in");
    }

    document.querySelector('#Email').value = "";
    document.querySelector('#Password').value = "";
});
