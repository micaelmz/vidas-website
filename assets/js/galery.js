var openMenuButton = $('.openMenu');
var closeButton = $('#closeButton');
function toggleMenu() {
     $('#menu').toggleClass('item_open');
     openMenuButton.toggleClass('close openMenu');
     $('#donationButton').toggle(); // Alterna a visibilidade do donationButton
     closeButton.toggle(); // Alterna a visibilidade do closeButton
     $('.logoToggle').toggle() // Alterna a visibilidade do logo
     return false;
}
openMenuButton.click(function() {
     toggleMenu();
     return false;
});

closeButton.click(function() {
     toggleMenu();
     return false;
});