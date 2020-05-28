function homeRedirect(){
    window.location.href = "/";
}


$('#search-button').click(function(){
    var opt = $("#translation-option :selected").text();
    var search = $.trim($('#search-word').val());
    // Edit searchWord

    $.ajax({
        url: "/search",
        type: 'GET',
        data = {"translation" : opt, "searchWord" : search },
        dataType: 'json', // added data type
        success: function(res) {
            console.log(res);
            alert(res);
        }
    });
})

$(window).on("load", function(){
    $('#spin-wrapper').delay(600).fadeOut("slow");
    $('.preloader').delay(600).fadeOut("slow");
    $('body').delay(50).css({'overflow':'visible'});
});


