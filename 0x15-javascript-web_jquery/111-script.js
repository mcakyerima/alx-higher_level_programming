// Allow DOM content to be fully loaded
$(document).ready(function () {
  // Add click event handler to the INPUT#btn_translate element
  $('#btn_translate').click(function () {
    // Get the language code entered by the user from INPUT#language_code
    var languageCode = $('#language_code').val();

    // Make a GET request to the translation API with the specified language code
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function (data) {
      // Update the text of the DIV#hello with the fetched translation
      $('#hello').text(data.hello);
    });
  });
});
