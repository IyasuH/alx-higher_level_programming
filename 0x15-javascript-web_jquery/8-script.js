$(document).ready(function() {
	$.get('https://swapi-api.hbtn.io/api/films/?format=json',  function(data) {
		let i = 0;
		while (i <= data.results.length){
			const movie_title = data.results[i].title;
			const content = $('<li></li>').text(movie_title);
			$('UL#list_movies').append(content);
			i++;
		}
	});
});

