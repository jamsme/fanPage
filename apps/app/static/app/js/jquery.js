$(document).ready(function() {

    $(".content").hover(function() {
        $("img.cont",this).css({"margin-bottom": "50px"});
    },
    function() {
        $("img.cont",this).css({"margin-bottom": "0px"});
    });

    $("div.navItems").hover(function() {
        $(this).css({"background-color": "#9e9e9ea3"});
    },
    function() {
        $(this).css({"background-color": "lightgrey"});
    });
    $('img#search').hover(function() {
        $(this).css({"border": "2px solid blue"});
    }, 
    function() {
        $(this).css({"border": "none"});
    });

});