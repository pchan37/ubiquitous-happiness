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

$('form :input').on('change input', function(){
    update();                
});


