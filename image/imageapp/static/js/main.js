$(document).ready(function () {

    $("html").niceScroll();

    $('.main-menu li a, .button-up a').bind('click',function(event){
        var $anchor = $(this);

        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1500,'easeInOutExpo');

        event.preventDefault();
    });

    $(document).scroll(function() {
        var y = $(this).scrollTop();
        if (y > 800) {
            $('.button-up a').fadeIn();
        } else {
            $('.button-up a').fadeOut();
        }
    });

    /*Form Label Animation*/
    $("input").on("focusout", function(){
        var content = $(this).val();
        var input = this;
        var name = input.name;
        if(content.length > 0 ){
            $("label[for='" + name + "']").addClass("not-empty");
        }
        else {
            $("label[for='" + name + "']").removeClass("not-empty");
        }
    });


});


/* Toggle between adding and removing the "active" and "show" classes when the user clicks on
 ne of the "Section" buttons. The "active" class is used to add a background color to the
 current button when its belonging panel is open. The "show" class is used to open the
 specific accordion panel */

$('.name-wrapper').auderoFlashingText({
    fadeIn: 500,
    duration: 800,
    fadeOut: 500,
    pause: 500,
    selection: 'descending',
    fontUnit: 'em',
    fontMinSize: 0.5,
    fontMaxSize: 1.5,
    strings: $('.name-wrapper > ul').children('li').map(function() {
        return $(this).text();
    })
});



