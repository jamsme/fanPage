$(document).ready(function() {

    $('#container').scroll(function() {
        $('#left').animate({top:$(this).scrollTop()});
    });

});