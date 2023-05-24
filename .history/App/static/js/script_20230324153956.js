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
//java-Modal FORM
function validateEmail(email){
    const regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9-]{2,4})+$/;
    return regex.test(email);
} 
// 3 card 
function validateForm4() {
    const name = document.getElementById("name").value;
    const age = document.getElementById("age").value;
    const email = document.getElementById("email").value;
    const phone = document.getElementById("phone").value;
    const address = document.getElementById("address").value;
    const exp = document.getElementById("exp").value;
    const skills = document.getElementById("skills").value;
    const file = document.getElementById("file").value;

    if (name =="") {
        swal("opps !", "Nome nao pode  estar vazio", "error");
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


//front end Modal FORM
function validateEmail2(email2){
    const regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9-]{2,4})+$/;
    return regex.test(email2);
}
function validateForm2() {
    const name2 = document.getElementById("name2").value;
    const age2 = document.getElementById("age2").value;
    const email2 = document.getElementById("email2").value;
    const phone2 = document.getElementById("phone2").value;
    const address2 = document.getElementById("address2").value;
    const exp2 = document.getElementById("exp2").value;
    const skills2 = document.getElementById("skills2").value;
    const file2 = document.getElementById("file2").value;

    if (name2 =="") {
        swal("opps !", "Name field can't be empty", "error");
        return false;
    }
    else if (name2 == name2.toUpperCase()) {
        document.getElementById('name2').value='';
        swal("name can't be UPPERCASE.", "info");
        return false;
    }
    else if (name2.split('').length < 2) {
        swal("Your full name is required", "info");
        return false;
    }

    
    else if (age2 =="") {
        swal("opps !", "Age field can't be empty", "error");
        return false;
    }
    else if ((age2 < 16) || (age2 > 65)) {
        document.getElementById('age2').value='';
        swal("opps !", "Age only between 16 and 65 Years old", "info");
        return false;
    }

    else if (email2 =="") {
        swal("opps !", "Email field can't be empty", "error");
        return false;
    }
    else if (!(validateEmail(email2))) {
        document.getElementById('email2').value='';
        swal("opps !", "type a valid email address", "error");
        return false;
    }

    else if (phone2 =="") {
        swal("opps !", "Phone field can't be empty", "error");
        return false;
    }
    else if (address2 =="") {
        swal("opps !", "Address field can't be empty", "error");
        return false;
    }
    else if (exp2 =="") {
        swal("opps !", "Experience field can't be empty", "error");
        return false;
    }
    else if (skills2 =="") {
        swal("opps !", "Skills field can't be empty", "error");
        return false;
    }
    else if (file2 =="") {
        swal("opps !", "File field can't be empty", "error");
        return false;
    }
    
}

//2) INPUT VALIDATION
//python-Modal FORM
function validateEmail(email){
    const regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9-]{2,4})+$/;
    return regex.test(email);
} 
// 2 card 
function validateForm7() {
    const name = document.getElementById("name").value;
    const age = document.getElementById("age").value;
    const email = document.getElementById("email").value;
    const phone = document.getElementById("phone").value;
    const address = document.getElementById("address").value;
    const exp = document.getElementById("exp").value;
    const skills = document.getElementById("skills").value;
    const file = document.getElementById("file").value;

    if (name =="") {
        swal("opps !", "Nome nao pode  estar vazio", "error");
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

// ------------- 3)
//maxim alowed file size
/*$(document).ready(function() {
    $("#file, #file2, #file3, #file4, #file5, #file6, #file7").bind('change', function(){
        var a = (this.files[0].size);

        if (5 * 999999) {
            swal('attention !', 'maximum allowed is 5mb', 'info');
            this.value ="";
        };
    });
});*/

// 4) allow only letter name
$(".name").keyup(function() {
    if (!/^[a-zA-Z _]*$/.test(this.value)){
        this.value = this.value.split(/[^a-zA-Z _]/).join('');
    }
})

// 5) prevent more than 5 spaces inside the field name
$(".name").on('keydown', function() {
    var $this =$(this);
    $(this).val($this.val().replace(/(\s{2,})|[^a-zA-Z0-9_']/g, ' ').replace(/^\s*/, ''));
})

// 6) prevent starting with space in all fields
$("input[type='text'], textarea").on("keypress", function(e) {
    if (e.which === 32 && ! this.value.length)
    e.preventDefault();
})

// 7) block letter in age field
$('.age').keyup(function() {
    if (!/^[0-9]*$/.test(this.value)) {
        this.value = this.value.split(/[^0-9]/).join('');
    }
})

// 8) block letter in phone field
$('.phone').keyup(function() {
    if (!/^[0-9]*$/.test(this.value)) {
        this.value = this.value.split(/[^0-9]/).join('');
    }
})

// 9) prevent starting by zero in age field
$(".age").on("input", function() {
    if(/^0/.test(this.value)) {
        this.value = this.value.replace(/^0/, "")
    }
})

// 10) convert UPPERCASE in LOWERCASE email input
$(document).ready(function() {
    $(".email").keyup(function() {
        this.value = this.value.toLowerCase();
    });
});


// 11) get TIME running at realtime
setInterval(function() {
    var date = new Date();
    $('#clock').html(
       (date.getHours() < 10 ? '0' : '') + date.getHours() + ":" +
       (date.getMinutes() < 10 ? '0' : '') + date.getMinutes() + ":" +
       (date.getSeconds() < 10 ? '0' : '') + date.getSeconds()
    );
}, 500);

// 12) update the page always at (00:00)
function autoRefresh(hours, minutes, seconds) {
    var now = new Date(), then = new Date();
    then.setHours(hours, minutes, seconds, 0);
    if(then.getTime() < now.getTime()) {
        then.setDate(now.getDate() + 1);
    }
    var timeout = (then.getTime() - now.getTime());
    setTimeout(function() {
        window.location.reload(true);
    }, timeout)
}
autoRefresh(0,0,0)