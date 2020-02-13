#!/usr/bin/node



$('#toggle_header').click(function(){
    if ($('header').hasClass('red')) {
        $('header').toggleClass('green');
    }
    else {
        $('header').toggleClass('red');
    }
})


$("header").addClass('red');