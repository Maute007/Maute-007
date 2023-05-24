//==========================================================
//# Script frontend (sem django block) 
//=====================================================

// 1) function pulse (login page)
(function pulse () {
    $('.txt-pulse').fadeOut(1000).fadeIn(1000, pulse);
})();

// 2) function validar email send
function validateForm() {
    var email = $('#email').val();
    var emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

    if (!emailRegex.test(email)) {
        swal("Email inválido", "error");
        $('#email').val("");
        return false;
    }

    else {
        return true;
    }
}


$(".btn-add").bind("click", validateForm);

// habilitar os butoes do popup 
//(somente quando tiver feito uma alteracao)


