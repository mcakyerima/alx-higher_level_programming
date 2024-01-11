// AllowDOM content to be fully loaded
$(document).ready(function () {
  // Function to fetch and display translation
  function fetchTranslation() {
    // Get the language code entered by the user from INPUT#language_code
    var languageCode = $('#language_code').val();

    // Make a GET request to the translation API with the specified language code
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function (data) {
      // Update the text of the DIV#hello with the fetched translation
      $('#hello').text(data.hello);
    });
  }

  // Attach click event handler to the INPUT#btn_translate element
  $('#btn_translate').click(fetchTranslation);

  // Attach keypress event handler to the INPUT#language_code element
  $('#language_code').keypress(function (event) {
    // Check if the pressed key is ENTER (key code 13)
    if (event.which === 13) {
      // Call the fetchTranslation function when ENTER is pressed
      fetchTranslation();
    }
  });
});
