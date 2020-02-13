document.addEventListener('DOMContentLoaded', function (event) {
  console.log('DOM fully loaded and parsed');

  $.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr'
  }).done((data) => {
    $('#hello').text(data.hello);
  });
});
