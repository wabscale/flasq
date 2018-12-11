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
