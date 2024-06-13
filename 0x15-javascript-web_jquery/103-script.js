/**
 * You should use this API service: https://www.fourtonfish.com/hellosalut/hello/
 * The language code will be the value entered in the tag INPUT#language_code
 * (ex: es, fr, en etc.)
 */

$(document).ready(function () {
  function fetchHello () {
    const langCode = $('#language_code').val();
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${langCode}`, function (data) {
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').click(fetchHello);

  $('#language_code').keypress(function (e) {
    if (e.which === 13) {
      fetchHello();
    }
  });
});
