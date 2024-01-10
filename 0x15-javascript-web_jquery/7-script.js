$('document').ready(function () {
  // Make an API GET request to the SWAPI url
  $.get(' https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    $('#character').text(data.name);
  });
});
