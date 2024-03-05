$(document).ready(function() {
    // Save Y Scrolling position
    let savedYPosition = parseInt(sessionStorage.getItem('yPosition')) || 0;
    // Scroll to saved position if existant or 0
    window.scrollTo(0, savedYPosition);
    // Free delivery text adjustment
    if (standardDelivery == 0 ){
        standardDelivery = 'FREE'
    } else {
        standardDelivery = standardDelivery.toFixed(2) + ' €'
    };
    // Adjust content of delivery label 0
    $('label[for="id_delivery_option_0"]').html(`<strong>Standard Delivery</strong> - ${standardDelivery} - <span class="lower-delivery">( 3 to 5 working days )</span>`);
    // Adjust content of delivery label 1
    $('label[for="id_delivery_option_1"]').html(`<strong>Express Delivery</strong> - ${expressDelivery.toFixed(2)} € - <span class="lower-delivery">( 2 to 3 working days )</span>`);
    // When form submitted ---
    $('form').submit(function(){
        // --- display loader 
        $('#loader-container').css("display", "flex");
    });
    // When deliveryy option changed
    $('#id_delivery_option_0, #id_delivery_option_1').change(function(){
        // read Y position
        let yPosition = window.scrollY;
        // save Y position
        sessionStorage.setItem('yPosition', yPosition);
        // submit form by clicking hidden button
        $('#delivery-button').click();
    });
});