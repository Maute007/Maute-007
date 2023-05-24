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
//   Modal FORM-COUT.HTML
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
        swal("opps !", "Campo Nome nao pode estar vazio", "error");
        return false;
    }
    else if (name == name.toUpperCase()) {
        document.getElementById('name').value='';
        swal("Nome nao pode estar em Maiusculas.", "info");
        return false;
    }
    else if (name.split('').length < 8) {
        swal("Digite o seu nome completo", "info");
        return false;
    }

    
    else if (age =="") {
        swal("opps !", "", "error");
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
//   Modal FORM-FRONT.HTML
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
//front end Modal FORM
function validateEmail3(email2){
    const regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9-]{2,4})+$/;
    return regex.test(email2);
}
function validateForm3() {
    const name3 = document.getElementById("name3").value;
    const age3 = document.getElementById("age3").value;
    const email3 = document.getElementById("email3").value;
    const phone3 = document.getElementById("phone3").value;
    const address3 = document.getElementById("address3").value;
    const exp3 = document.getElementById("exp3").value;
    const skills3 = document.getElementById("skills3").value;
    const file3 = document.getElementById("file3").value;

    if (name3 =="") {
        swal("opps !", "Name field can't be empty", "error");
        return false;
    }
    else if (name3 == name3.toUpperCase()) {
        document.getElementById('name3').value='';
        swal("name can't be UPPERCASE.", "info");
        return false;
    }
    else if (name3.split('').length < 2) {
        swal("Your full name is required", "info");
        return false;
    }
    
    else if (age3 =="") {
        swal("opps !", "Age field can't be empty", "error");
        return false;
    }
    else if ((age3 < 16) || (age3 > 65)) {
        document.getElementById('age3').value='';
        swal("opps !", "Age only between 16 and 65 Years old", "info");
        return false;
    }

    else if (email3 =="") {
        swal("opps !", "Email field can't be empty", "error");
        return false;
    }
    else if (!(validateEmail3(email3))) {
        document.getElementById('email3').value='';
        swal("opps !", "type a valid email address", "error");
        return false;
    }

    else if (phone3 =="") {
        swal("opps !", "Phone field can't be empty", "error");
        return false;
    }
    else if (address3 =="") {
        swal("opps !", "Address field can't be empty", "error");
        return false;
    }
    else if (exp3 =="") {
        swal("opps !", "Experience field can't be empty", "error");
        return false;
    }
    else if (skills3 =="") {
        swal("opps !", "Skills field can't be empty", "error");
        return false;
    }
    else if (file3 =="") {
        swal("opps !", "File field can't be empty", "error");
        return false;
    }
    
}
//java Modal FORM
//   FORM-JAVA.HTML
function validateEmail4(email4){
    const regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9-]{2,4})+$/;
    return regex.test(email4);
}
function validateForm4() {
    const name4 = document.getElementById("name4").value;
    const age4 = document.getElementById("age4").value;
    const email4 = document.getElementById("email4").value;
    const phone4 = document.getElementById("phone4").value;
    const address4 = document.getElementById("address4").value;
    const exp4 = document.getElementById("exp4").value;
    const skills4 = document.getElementById("skills4").value;
    const file4 = document.getElementById("file4").value;

    if (name4 =="") {
        swal("opps !", "Name field can't be empty", "error");
        return false;
    }
    else if (name4 == name4.toUpperCase()) {
        document.getElementById('name4').value='';
        swal("name can't be UPPERCASE.", "info");
        return false;
    }
    else if (name4.split('').length < 2) {
        swal("Your full name is required", "info");
        return false;
    }

    
    else if (age4 =="") {
        swal("opps !", "Age field can't be empty", "error");
        return false;
    }
    else if ((age4 < 16) || (age4 > 65)) {
        document.getElementById('age4').value='';
        swal("opps !", "Age only between 16 and 65 Years old", "info");
        return false;
    }

    else if (email4 =="") {
        swal("opps !", "Email field can't be empty", "error");
        return false;
    }
    else if (!(validateEmail4(email4))) {
        document.getElementById('email4').value='';
        swal("opps !", "type a valid email address", "error");
        return false;
    }

    else if (phone4 =="") {
        swal("opps !", "Phone field can't be empty", "error");
        return false;
    }
    else if (address4 =="") {
        swal("opps !", "Address field can't be empty", "error");
        return false;
    }
    else if (exp4 =="") {
        swal("opps !", "Experience field can't be empty", "error");
        return false;
    }
    else if (skills4 =="") {
        swal("opps !", "Skills field can't be empty", "error");
        return false;
    }
    else if (file4 =="") {
        swal("opps !", "File field can't be empty", "error");
        return false;
    }
    
}
//Modal FORM-LOGIS.HTML
function validateEmail5(email5){
    const regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9-]{2,4})+$/;
    return regex.test(email5);
}
function validateForm5() {
    const name5 = document.getElementById("name5").value;
    const age5 = document.getElementById("age5").value;
    const email5 = document.getElementById("email5").value;
    const phone5 = document.getElementById("phone5").value;
    const address5 = document.getElementById("address5").value;
    const exp5 = document.getElementById("exp5").value;
    const skills5 = document.getElementById("skills5").value;
    const file5 = document.getElementById("file5").value;

    if (name5 =="") {
        swal("opps !", "Name field can't be empty", "error");
        return false;
    }
    else if (name5 == name5.toUpperCase()) {
        document.getElementById('name2').value='';
        swal("name can't be UPPERCASE.", "info");
        return false;
    }
    else if (name5.split('').length < 2) {
        swal("Your full name is required", "info");
        return false;
    }
    
    else if (age5 =="") {
        swal("opps !", "Age field can't be empty", "error");
        return false;
    }
    else if ((age5 < 16) || (age5 > 65)) {
        document.getElementById('age5').value='';
        swal("opps !", "Age only between 16 and 65 Years old", "info");
        return false;
    }

    else if (email5 =="") {
        swal("opps !", "Email field can't be empty", "error");
        return false;
    }
    else if (!(validateEmail5(email5))) {
        document.getElementById('email5').value='';
        swal("opps !", "type a valid email address", "error");
        return false;
    }

    else if (phone5 =="") {
        swal("opps !", "Phone field can't be empty", "error");
        return false;
    }
    else if (address5 =="") {
        swal("opps !", "Address field can't be empty", "error");
        return false;
    }
    else if (exp5 =="") {
        swal("opps !", "Experience field can't be empty", "error");
        return false;
    }
    else if (skills5 =="") {
        swal("opps !", "Skills field can't be empty", "error");
        return false;
    }
    else if (file5 =="") {
        swal("opps !", "File field can't be empty", "error");
        return false;
    }
    
}
// Modal FORM-MANAGE.HTML
function validateEmail6(email6){
    const regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9-]{2,4})+$/;
    return regex.test(email6);
}
function validateForm6() {
    const name6 = document.getElementById("name6").value;
    const age6 = document.getElementById("age6").value;
    const email6 = document.getElementById("email6").value;
    const phone6 = document.getElementById("phone6").value;
    const address6 = document.getElementById("address6").value;
    const exp6 = document.getElementById("exp6").value;
    const skills6 = document.getElementById("skills6").value;
    const file6 = document.getElementById("file6").value;

    if (name6 =="") {
        swal("opps !", "Name field can't be empty", "error");
        return false;
    }
    else if (name6 == name6.toUpperCase()) {
        document.getElementById('name6').value='';
        swal("name can't be UPPERCASE.", "info");
        return false;
    }
    else if (name6.split('').length < 2) {
        swal("Your full name is required", "info");
        return false;
    }

    
    else if (age6 =="") {
        swal("opps !", "Age field can't be empty", "error");
        return false;
    }
    else if ((age6 < 16) || (age6 > 65)) {
        document.getElementById('age2').value='';
        swal("opps !", "Age only between 16 and 65 Years old", "info");
        return false;
    }

    else if (email6 =="") {
        swal("opps !", "Email field can't be empty", "error");
        return false;
    }
    else if (!(validateEmail6(email6))) {
        document.getElementById('email6').value='';
        swal("opps !", "type a valid email address", "error");
        return false;
    }

    else if (phone6 =="") {
        swal("opps !", "Phone field can't be empty", "error");
        return false;
    }
    else if (address6 =="") {
        swal("opps !", "Address field can't be empty", "error");
        return false;
    }
    else if (exp6 =="") {
        swal("opps !", "Experience field can't be empty", "error");
        return false;
    }
    else if (skills6 =="") {
        swal("opps !", "Skills field can't be empty", "error");
        return false;
    }
    else if (file6 =="") {
        swal("opps !", "File field can't be empty", "error");
        return false;
    }
    
}
// Modal FORM-PYTHON.HTML
function validateEmail7(email7){
    const regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9-]{2,4})+$/;
    return regex.test(email7);
}
function validateForm7() {
    const name7 = document.getElementById("name7").value;
    const age7 = document.getElementById("age7").value;
    const email7 = document.getElementById("email7").value;
    const phone7 = document.getElementById("phone7").value;
    const address7 = document.getElementById("address7").value;
    const exp7 = document.getElementById("exp7").value;
    const skills7 = document.getElementById("skills7").value;
    const file7 = document.getElementById("file7").value;

    if (name7 =="") {
        swal("opps !", "Name field can't be empty", "error");
        return false;
    }
    else if (name7 == name7.toUpperCase()) {
        document.getElementById('name7').value='';
        swal("name can't be UPPERCASE.", "info");
        return false;
    }
    else if (name7.split('').length < 2) {
        swal("Your full name is required", "info");
        return false;
    }
    
    else if (age7 =="") {
        swal("opps !", "Age field can't be empty", "error");
        return false;
    }
    else if ((age7 < 16) || (age7 > 65)) {
        document.getElementById('age7').value='';
        swal("opps !", "Age only between 16 and 65 Years old", "info");
        return false;
    }

    else if (email7 =="") {
        swal("opps !", "Email field can't be empty", "error");
        return false;
    }
    else if (!(validateEmail7(email7))) {
        document.getElementById('email7').value='';
        swal("opps !", "type a valid email address", "error");
        return false;
    }

    else if (phone7 =="") {
        swal("opps !", "Phone field can't be empty", "error");
        return false;
    }
    else if (address7 =="") {
        swal("opps !", "Address field can't be empty", "error");
        return false;
    }
    else if (exp7 =="") {
        swal("opps !", "Experience field can't be empty", "error");
        return false;
    }
    else if (skills7 =="") {
        swal("opps !", "Skills field can't be empty", "error");
        return false;
    }
    else if (file7 =="") {
        swal("opps !", "File field can't be empty", "error");
        return false;
    }
    
}

// ------------- 3)
//maxim alowed file size
$(document).ready(function() {
    $("#file, #file2, #file3, #file4, #file5, #file6, #file7").bind('change', function(){
        var a = (this.files[0].size);

        if (a >  5 * 1024 * 1024) {
            swal('Atenção !', 'O maximo permitido sao 5mb', 'info');
            this.value ="";
        };
    });
});

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

