$(document).ready(function() {
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
