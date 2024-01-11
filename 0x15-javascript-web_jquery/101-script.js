// Wait for DOM content to be fully loaded
$(document).ready(function () {
  // Attach click event handlers to the relevant DIV elements
  $('#add_item').click(function () {
    // Add a new <li> element with the text "Item" to UL.my_list
    $('<li>').text('Item').appendTo('ul.my_list');
  });

  $('#remove_item').click(function () {
    // Remove the last <li> element from UL.my_list
    $('ul.my_list li:last-child').remove();
  });

  $('#clear_list').click(function () {
    // Remove all <li> elements from UL.my_list
    $('ul.my_list').empty();
  });
});
