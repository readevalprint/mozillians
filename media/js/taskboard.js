$(document).ajaxSend(function(event, xhr, settings) {
    /* Hide or display input when a user is slelected. */
    $("#id_contact_on_deck").bind('added',function() {
        $("#id_contact_text").hide();
    });
    $("#id_contact_on_deck").bind('killed',function() {
        $("#id_contact_text").show();
    });
});
