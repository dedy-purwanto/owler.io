$(function(){
    $("#id_signature").change(function(){
        if($(this).val() == 1){
            $("#id_signature_text").show();
        }else{
            $("#id_signature_text").hide();
        }
    });
    $("#id_signature").trigger("change");
});
