$('document').ready(function () {
  // Add a click event to toggle DIV#toggle_header
  $('#toggle_header').click(function () {
    // toggle class "red" and "green" inside <header>
    $('header').toggleClass('red green');
  });
});
