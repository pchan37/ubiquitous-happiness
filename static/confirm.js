var $form = $('form');

var checker = function(){
    var email = document.getElementById('email');
    var conf = document.getElementById('confirmEmail');
    if ( email.value != conf.value ){
        document.getElementById('submitData').value = "Cannot Submit! Emails do not match!";
        $('#submitData').attr('disabled', 'disabled');
    }else{
        document.getElementById('submitData').value = "submit";
        $('#submitData').removeAttr('disabled');
    };
};

$('form :input').on('change input', function(){
    checker();
});


