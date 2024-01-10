$('document').ready(function () {
  // make an API request to SWAPI api
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    data.results.forEach(function (movie) {
      // create a new list item with the movie title and append to list
      $('<li>').text(movie.title).appendTo('#list_movies');
    });
  });
});
