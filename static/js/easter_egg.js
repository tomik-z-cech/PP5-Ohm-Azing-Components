$(document).ready(function() {
// keep track of the keys pressed
let secretCode = '';

// Attach keydown event listener to the document
$(document).keydown(function(event) {
        // Append the pressed key to the key sequence
        secretCode += event.key;
        // Check if the key sequence matches the specified string
        if (secretCode.includes('ilovetocode')) {
        // Show an alert window
        alert('Great ! Enjoy 75% discount with code DJANGO75 valid through 2024 !');
        // Reset the key sequence for the next input
        secretCode = '';
        }
    });
});