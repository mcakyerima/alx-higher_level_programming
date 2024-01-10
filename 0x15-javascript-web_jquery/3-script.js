$('document').ready(function () {
  //Attach a click event handler to DIV#red_header
  $('#red_header').click(function () {
    // Add the red class
    $('header').addClass('red');
  });
});
