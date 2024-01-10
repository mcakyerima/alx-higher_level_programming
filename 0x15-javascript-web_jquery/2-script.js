$(document).ready(function () {
  // Add a click event to DIV#red_header
  $('#red_header').click(function () {
    // Select the <header> element and  update
    $('header').css('color', '#FF0000');
  });
});
