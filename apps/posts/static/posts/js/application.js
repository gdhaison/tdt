$('#cmt').keypress(function (e) {
  if (e.which == 13) {
    $('form#form-cmt').submit();
    return false;
  }
});
