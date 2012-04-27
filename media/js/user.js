$(function(){
  /* Autoselect API key text. */
  $("#api-key").click(function() {
    this.select();
  }).change(function() {
    $(this).val($(this).data('value'));
  }).keydown(function() {
    $(this).val($(this).data('value'));
  }).keyup(function() {
    $(this).val($(this).data('value'));
  });
});


