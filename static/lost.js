var $form = $('form'),
    origForm = $form.serialize();

var update = function(){
    //var input = document.getElementById(formData);
    var str = $( "form" ).serializeArray();
    $.post("/updateLost/", {formData: JSON.stringify(str)}, function(response){
        console.log(response);
        var formContent = document.getElementsByClassName('contentData');
        formContent[0].innerHTML = response;
            
    } );
    
};

var checkSubmission = function(){
    var contentData = document.getElementsByClassName('dataObject');
    console.log(contentData);
    if( contentData.length < 5){
        $('#submitData').removeAttr('disabled');
    }else{
        $('#submitData').attr('disabled','disabled');
    }
};



$('form :input').on('change input', function(){
    update();
    checkSubmission();
});



