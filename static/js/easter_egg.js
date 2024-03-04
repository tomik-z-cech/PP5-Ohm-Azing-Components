$(document).ready(function() {
// keep track of the keys pressed
let secretCode = '';

// Attach keydown event listener to the document
$(document).keydown(function(event) {
        // Append the pressed key to the key sequence
        secretCode += event.key;
        console.log(secretCode);

        // Check if the key sequence matches the specified string
        if (secretCode.includes('ilovetocode')) {
        // Show an alert window
        alert('Great ! Enjoy 50% discount with code CI50 !');
        // Reset the key sequence for the next input
        secretCode = '';
        }
    });
});