$('document').ready(function () {
  // Add a click event to DIV#add_item
  $('#add_item').click(function () {
    // create a new <li> element with a text "Item"
    let newItem = $('<li>').text('Item');

    // Append the new <li> to the UL.my_list
    $('ul.my_list').append(newItem);
  });
});
