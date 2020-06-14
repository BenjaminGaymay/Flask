$('a[href^="#"]').click(function(){
	var the_id = $(this).attr("href");
	var padding = parseInt($("nav").height(), 10) + parseInt($("nav").css("padding-top"), 10);

	$('html, body').animate({
		scrollTop:$(the_id).offset().top - padding
	}, 'slow');
	return false;
});


$(window).on('resize load', function() {
	var bodyPadding = parseInt($("nav").height(), 10) + parseInt($("nav").css("padding-top"), 10);

	$('body').css({
	   "padding-top": bodyPadding + "px"
	});

	$(".separator").first("p").css({
		"margin-top": "0"
	});

});
