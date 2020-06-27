function homeRedirect(){
    window.location.href = "/";
}

$(window).on("load", function(){
    
    $('#spin-wrapper').delay(600).fadeOut("slow");
    $('.preloader').delay(600).fadeOut("slow");
    $('body').delay(50).css({'overflow':'visible'});
});


$('#search-button').click(function(){

    var opt = $("#translation-option :selected").text();
    var translate = $.trim($('#search-word').val());

    var Obj = { search : translate };
    
    $.ajax({
        url: "http://127.0.0.1:8000/api/translations/",
        type: 'GET',
        data : Obj,
        dataType: 'json', // added data type
        success: function(res) {
            console.log(res);
            alert(res);
        },
        error: function (request, status, error) {
            alert(request.responseText);
        }
    });
});




