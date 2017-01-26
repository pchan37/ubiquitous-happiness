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



$(document).ready( function() {
        $(document).on('change', '.btn-file :file', function() {
        var input = $(this),
            label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
        input.trigger('fileselect', [label]);
        });
        $('.btn-file :file').on('fileselect', function(event, label) {
            var input = $(this).parents('.input-group').find(':text'),
                log = label; 
            if( input.length ) {
                input.val(log);
            } else {
                if( log ) alert(log);
            }
        });
        function readURL(input) {
            if (input.files && input.files[0]) {
                var reader = new FileReader();
                reader.onload = function (e) {
                    $('#img-upload').attr('src', e.target.result);
                }
                reader.readAsDataURL(input.files[0]);
            }
        }
        $("#imgInp").change(function(){
            readURL(this);
        });     
    });
