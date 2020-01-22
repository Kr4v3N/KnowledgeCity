(function ($) {
    "use strict";
    // [ Simple slide100 ]*/

    $('.simpleslide100').each(function(){
        let delay = 7000;
        let speed = 1000;
        let itemSlide = $(this).find('.simpleslide100-item');
        let nowSlide = 0;

        $(itemSlide).hide();
        $(itemSlide[nowSlide]).show();
        nowSlide++;
        if(nowSlide >= itemSlide.length) {nowSlide = 0;}

        setInterval(function(){
            $(itemSlide).fadeOut(speed);
            $(itemSlide[nowSlide]).fadeIn(speed);
            nowSlide++;
            if(nowSlide >= itemSlide.length) {nowSlide = 0;}
        },delay);
    });


})(jQuery);