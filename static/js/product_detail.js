$(document).ready(function() {
    // variable for reading value
    let inputField = $('#quantity');
    // if empty assign value 1
    if (inputField.val() == '') {
        inputField.val(1);
    };
    // if plus clicked
    $('.plus').click(function() {
        // quantity ++ max stockAmount
        if (inputField.val() < stockAmount ){
            inputField.val(parseInt(inputField.val(), 10) + 1);
        };
    });
    // if minus clicked
    $('.minus').click(function() {
        // quantity -- min 0 
        if (inputField.val() > 1 ){
            inputField.val(parseInt(inputField.val(), 10) - 1);
        };
    });
    // If second image hovered
    $('#img2').hover(function() {
        // Set it large
        $('#img2').removeClass('image-small').addClass('image-large');
        // Set the other images small
        $('#img1, #img3').removeClass('image-large').addClass('image-small');
    });
    // If third image hovered
    $('#img3').hover(function() {
        // Set it large
        $('#img3').removeClass('image-small').addClass('image-large');
        // Set the other images small
        $('#img1, #img2').removeClass('image-large').addClass('image-small');
    });
    // If first image hovered
    $('#img1').hover(function() {
        // Set it large
        $('#img1').removeClass('image-small').addClass('image-large');
        // Set the other images small
        $('#img2, #img3').removeClass('image-large').addClass('image-small');
    });
});
