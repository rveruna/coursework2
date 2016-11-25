(function(){


    var windowWidth = function() {
        var e = window,
        a = 'inner';

        if ( !( 'innerWidth' in window ) ) {
            a = 'client';
            e = document.documentElement || document.body;
        }
        return e[ a+'Width' ];
    }

    var carouselPadding = function() {

        var limit =  1690;
        if ( Modernizr.mq("( min-width: " + limit + "px ) ") ) {

            padding = Math.round( ( windowWidth() - limit ) / 2 );

        }

        else {

            padding = 0;

        }

        return padding;
    };

    var owl = $(".carousel");

    owl.owlCarousel({

        items : 1,
        loop : true,
        // margin : 10,
        nav : false,
        dots : true,
        responsive :  {
            0  : {
                stagePadding : 0
            },
            1690 : {
                stagePadding : carouselPadding(),
                margin : 30
            },
        }
    });

    $('.owl-item:not(".active")').on('click', function(e) {

    	if ( $(this).next().is('.active') ) {
			owl.trigger('next.owl.carousel');
    	}

    	else {
			owl.trigger('prev.owl.carousel');
    	}
    });


}());
