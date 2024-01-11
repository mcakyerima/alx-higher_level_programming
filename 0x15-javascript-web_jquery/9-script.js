$('document').ready(function () {
  // make a GET request to the translation API
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    // update DIV #hello with the translation.
    $('#hello').text(data.hello);
  });
});
