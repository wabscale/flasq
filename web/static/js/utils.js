function createForm(o) {
    let $tr = $(o).closest('tr');
    let $form = $('<form method="POST"></form>');
    $form.append($tr.find('input[name="id"]'));
    let $hidden_csrf = $('<input type="hidden" name="csrf_token"/>');
    $hidden_csrf.val(csrf_token.value);
    $form.append($hidden_csrf);
    return $form;
}

$(document).ready(function() {
    var navbar = document.getElementById("top-navbar");
    var nav_items = navbar.getElementsByTagName('a');
    
    for (var i=0; i<nav_items.length; ++i) {
        if (nav_items.item(i).href.toString() == document.location.toString()) {
            nav_items.item(i).className += " active";
            break;
        }
    }
});
