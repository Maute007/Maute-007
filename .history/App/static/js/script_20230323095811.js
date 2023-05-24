/* --------------------------------------------- 
# SCRIPTS 
--------------------------------------------- */

// 1) Script to auto close the alert after 3s
window.setTimeout(function() {
    $(".alert").fadeTo(500, 0).slideUp(500, function() {
        $(this).remove();
    });
}, 3000);

//2) INPUT VALIDATION
//counterModal FORM
function validateEmail(email){
    const regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9-]{2,4})+$/;
    return regex.test(email);
}
function validateForm() {
    const name = document.getElementById("name").value;
    const age = document.getElementById("age").value;
    const email = document.getElementById("email").value;
    const phone = document.getElementById("phone").value;
    const address = document.getElementById("address").value;
    const exp = document.getElementById("exp").value;
    const skills = document.getElementById("skills").value;
    const file = document.getElementById("file").value;

    if (name =="") {
        swal("opps !", "Name nao pode  ", "error");
        return false;
    }
    else if (name == name.toUpperCase()) {
        document.getElementById('name').value='';
        swal("Nome nao pode estar em Maiusculas.", "info");
        return false;
    }
    else if (name.split('').length < 2) {
        swal("Your full name is required", "info");
        return false;
    }

    
    else if (age =="") {
        swal("opps !", "Age field can't be empty", "error");
        return false;
    }
    else if ((age < 16) || (age > 65)) {
        document.getElementById('age').value='';
        swal("opps !", "Age only between 16 and 65 Years old", "info");
        return false;
    }

    else if (email =="") {
        swal("opps !", "Email field can't be empty", "error");
        return false;
    }
    else if (!(validateEmail(email))) {
        document.getElementById('email').value='';
        swal("opps !", "type a valid email address", "error");
        return false;
    }

    else if (phone =="") {
        swal("opps !", "Phone field can't be empty", "error");
        return false;
    }
    else if (address =="") {
        swal("opps !", "Address field can't be empty", "error");
        return false;
    }
    else if (exp =="") {
        swal("opps !", "Experience field can't be empty", "error");
        return false;
    }
    else if (skills =="") {
        swal("opps !", "Skills field can't be empty", "error");
        return false;
    }
    else if (file =="") {
        swal("opps !", "File field can't be empty", "error");
        return false;
    }
    
}
