$(document).ready(function() {
    $('#img2').hover(function() {
        $('#img2').removeClass('image-small').addClass('image-large');
        $('#img1, #img3').removeClass('image-large').addClass('image-small');
    });
    $('#img3').hover(function() {
        $('#img3').removeClass('image-small').addClass('image-large');
        $('#img1, #img2').removeClass('image-large').addClass('image-small');
    });
    $('#img1').hover(function() {
        $('#img1').removeClass('image-small').addClass('image-large');
        $('#img2, #img3').removeClass('image-large').addClass('image-small');
    });
});
