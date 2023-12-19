document.querySelector('.Losave').addEventListener('click', (event) => {
    event.preventDefault();
    let Name = document.querySelector('input[name="Name"]').value;
    let phno = document.querySelector('input[name="phno"]').value;
    let dob = document.querySelector('input[name="dob"]').value;
    let email = document.querySelector('input[name="email"]').value;
    let password = document.querySelector('input[name="password"]').value;

    let loginDetails = localStorage.getItem("login");

    if (loginDetails === null) {
        let passwordJSON = [];
        passwordJSON.push({ Name, phno, dob, email, password });
        localStorage.setItem("login", JSON.stringify(passwordJSON));
    } else {
        let passwordJSON = JSON.parse(loginDetails);
        passwordJSON.push({ Name, phno, dob, email, password });
        localStorage.setItem("login", JSON.stringify(passwordJSON));
    }

    alert("Details Saved");

    // Clear input fields after saving
    document.querySelector('input[name="Name"]').value = "";
    document.querySelector('input[name="phno"]').value = "";
    document.querySelector('input[name="dob"]').value = "";
    document.querySelector('input[name="email"]').value = "";
    document.querySelector('input[name="password"]').value = "";
});
