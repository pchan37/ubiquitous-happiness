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

var upload = function(){
    var fileList = document.getElementById('fileUpload').files;
    var formData = new FormData();
    formData.append("imgFile", fileList[0]);
    $.ajax({
        url: '/uploadImage/',
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success : function(response){
            console.log(response);
            document.getElementById('imgURL').value = response;
        }
    });
};

document.getElementById('fileUpload').onchange = function(event){
    upload();
};

