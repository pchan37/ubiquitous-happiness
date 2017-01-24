var $form = $('form'),
    origForm = $form.serialize();

var update = function(){
    //var input = document.getElementById(formData);
    var str = $( "form" ).serializeArray();    
    $.get("/updateFound", {"formData" : str}, function(d){ console.log("success"); } );
};


$('form :input').on('change input', function(){
    if ($form.serialize() != origForm){
	update();
    }
});



