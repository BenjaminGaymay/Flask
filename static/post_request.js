$(".music").click(function(e){

	var postRequest = {
		"music": $(e.target).text(),
		"secret": "1w4ntMu5ik"
	};

	$.ajax({
		url:"/musiques",
		type:'POST',
		crossDomain: true,
		dataType: 'json',
		contentType: 'application/json',
		data:JSON.stringify(postRequest)
	});
});
