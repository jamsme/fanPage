$(document).ready(function() {

    $(".content").hover(function() {
        $("button#delete",this).css({"display": "unset"})
    },
    function() {
        $("button#delete",this).css({"display": "none"})
    });

    $("div.navItems").hover(function() {
        $(this).css({"background-color": "#9e9e9ea3"});
    },
    function() {
        $(this).css({"background-color": "lightgrey"});
    });

    $('div#hold').hover(function() {
        $("input#add",this).css({"display": "unset"});
    }, 
    function() {
        $("input#add",this).css({"display": "none"});
    });

});