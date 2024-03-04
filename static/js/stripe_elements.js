// Keys
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
// Styling
let style = {
    base: {
        iconColor: '#fafafa',
        color: '#fafafa',
        fontFamily: 'Ideal Sans, system-ui, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#fafafa'
        }
    },
    invalid: {
        color: '#ff3333',
        iconColor: '#ff3333'
    }
};

// Payment element mounting
var card = elements.create('card',{ 
    style: style
});

$(document).ready(function() {
    // if ENTER pressed - submit form
    $(document).keypress(function(event) {
        // Check if the pressed key is Enter (key code 13)
        if (event.which === 13) {
            // act as submit payment button clicked
            console.log('enter')
            $('#submit-payment').click();
        }
    });
    // Mount card element
    card.mount('#card-element');
    // Validation of card
    card.addEventListener('change', function (event) {
        let errorDiv = $('#card-errors');
        if (event.error) {
            var html = `
                <span role="alert" class="card-error-message">
                <i class="bi bi-x-circle"></i>
                ${event.error.message}</span>
            `;
            $(errorDiv).html(html);
        } else {
            errorDiv.textContent = '';
        }
    });

    // When submit payment button is clicked
    $('#submit-payment').click(function(ev) {
        // prevent default
        ev.preventDefault();
        // disable card panel
        card.update({ 'disabled': true});
        // if any required fields are empty or in incorrect format 
        if ($('#id_first_name').val() === '' || $('#id_last_name').val() === '' || $('#id_phone_number').val() === '' 
        || !/^\d+$/.test($('#id_phone_number').val()) || $('#id_email_order').val() === '' || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test($('#id_email_order').val())
        || $('#id_address_1').val() === '' || $('#id_city').val() === '' || $('#id_county').val() === '' || $('#id_post_code').val() === ''
        || $('#id_address_1').val() === '') {
            // if first name field empty
            if ($('#id_first_name').val() === '') {
                // highlight the incorrect field
                $('#id_first_name').attr('style', 'border: 1px solid var(--negative-foreground) !important');
                // scroll to the field with animation of 100ms
                $('html, body').animate({
                    scrollTop: $('#id_first_name').offset().top - 50
                }, 100);
                // remove the highlight after 3s
                setTimeout(function() {
                    $('#id_first_name').removeAttr('style');
                }, 3000);
            };
            // if last name field empty
            if ($('#id_last_name').val() === '') {
                // highlight the incorrect field
                $('#id_last_name').attr('style', 'border: 1px solid var(--negative-foreground) !important');
                // scroll to the field with animation of 100ms
                $('html, body').animate({
                    scrollTop: $('#id_last_name').offset().top - 50
                }, 100);
                // remove the highlight after 3s
                setTimeout(function() {
                    $('#id_last_name').removeAttr('style');
                }, 3000);
            };
            // if phone number field empty or doesn't contain only numbers
            if ($('#id_phone_number').val() === '' || !/^\d+$/.test($('#id_phone_number').val())) {
                // highlight the incorrect field
                $('#id_phone_number').attr('style', 'border: 1px solid var(--negative-foreground) !important');
                // scroll to the field with animation of 100ms
                $('html, body').animate({
                    scrollTop: $('#id_phone_number').offset().top - 50
                }, 100);
                // remove the highlight after 3s
                setTimeout(function() {
                    $('#id_phone_number').removeAttr('style');
                }, 3000);
            };
            // if email field empty or contains incorrect email address format
            if ($('#id_email_order').val() === '' || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test($('#id_email_order').val())){
                // highlight the incorrect field
                $('#id_email_order').attr('style', 'border: 1px solid var(--negative-foreground) !important');
                // scroll to the field with animation of 100ms
                $('html, body').animate({
                    scrollTop: $('#id_email_order').offset().top - 50
                }, 100);
                // remove the highlight after 3s
                setTimeout(function() {
                    $('#id_email_order').removeAttr('style');
                }, 3000);
            };
            // if first line of address field empty
            if ($('#id_address_1').val() === '') {
                // highlight the incorrect field
                $('#id_address_1').attr('style', 'border: 1px solid var(--negative-foreground) !important');
                // scroll to the field with animation of 100ms
                $('html, body').animate({
                    scrollTop: $('#id_address_1').offset().top - 50
                }, 100);
                // remove the highlight after 3s
                setTimeout(function() {
                    $('#id_address_1').removeAttr('style');
                }, 3000);
            };
            // if city field empty
            if ($('#id_city').val() === '') {
                // highlight the incorrect field
                $('#id_city').attr('style', 'border: 1px solid var(--negative-foreground) !important');
                // scroll to the field with animation of 100ms
                $('html, body').animate({
                    scrollTop: $('#id_city').offset().top - 50
                }, 100);
                // remove the highlight after 3s
                setTimeout(function() {
                    $('#id_city').removeAttr('style');
                }, 3000);
            };
            // if county field empty
            if ($('#id_county').val() === '') {
                // highlight the incorrect field
                $('#id_county').attr('style', 'border: 1px solid var(--negative-foreground) !important');
                // scroll to the field with animation of 100ms
                $('html, body').animate({
                    scrollTop: $('#id_county').offset().top - 50
                }, 100);
                // remove the highlight after 3s
                setTimeout(function() {
                    $('#id_county').removeAttr('style');
                }, 3000);
            };
            // if post code field empty
            if ($('#id_post_code').val() === '') {
                // highlight the incorrect field
                $('#id_post_code').attr('style', 'border: 1px solid var(--negative-foreground) !important');
                // scroll to the field with animation of 100ms
                $('html, body').animate({
                    scrollTop: $('#id_post_code').offset().top - 50
                }, 100);
                // remove the highlight after 3s
                setTimeout(function() {
                    $('#id_post_code').removeAttr('style');
                }, 3000);
            };
            // if country field empty
            if ($('#id_country').val() === '') {
                // highlight the incorrect field
                $('#id_country').attr('style', 'border: 1px solid var(--negative-foreground) !important');
                // scroll to the field with animation of 100ms
                $('html, body').animate({
                    scrollTop: $('#id_country').offset().top - 50
                }, 100);
                // remove the highlight after 3s
                setTimeout(function() {
                    $('#id_country').removeAttr('style');
                }, 3000);
            };
        } else {
        // All field filled in correctly
            // Display loader
            $('#loader-container').css("display", "flex");
            // Disable submit payment button
            $('#submit-payment').attr('disabled', true);
            // Create postData
            var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
            var postData = {
                'csrfmiddlewaretoken': csrfToken,
                'client_secret': clientSecret,
                'save_info': $('#save-details').val(),
            };
            // URL for postData
            var url = '/checkout/check-checkout-data/';
            // Once data posted ...
            $.post(url, postData).done(function () {
                // Create data for Stripe Payment
                stripe.confirmCardPayment(clientSecret, {
                    payment_method: {
                        card: card,
                        billing_details: {
                            name: $.trim(form.first_name.value) + ' ' + $.trim(form.last_name.value),
                            phone: $.trim(form.phone_number.value),
                            email: $.trim(form.email.value),
                            address:{
                                line1: $.trim(form.address_1.value),
                                line2: $.trim(form.address_2.value),
                                city: $.trim(form.city.value),
                                country: $.trim(form.country.value),
                                state: $.trim(form.county.value),
                            }
                        }
                    },
                    shipping: {
                        name: $.trim(form.first_name.value) + ' ' + $.trim(form.last_name.value),
                        phone: $.trim(form.phone_number.value),
                        address: {
                            line1: $.trim(form.address_1.value),
                            line2: $.trim(form.address_2.value),
                            city: $.trim(form.city.value),
                            country: $.trim(form.country.value),
                            postal_code: $.trim(form.post_code.value),
                            state: $.trim(form.county.value),
                        }
                    },
                // then return result
                }).then(function(result) {
                    console.log('error')
                    // Error result
                    if (result.error) {
                        // Display error message
                        $('#card-errors').html(`
                            <span role="alert" class="card-error-message">
                            <i class="bi bi-x-circle"></i>
                            ${result.error.message}</span>
                            `
                        );
                        // Hide loader
                        $('#loader-container').css("display", "none");
                        // Enable card input
                        card.update({ 'disabled': false});
                        // Enable submit button
                        $('#submit-payment').attr('disabled', false);
                    } else {
                        // If payment successful
                        if (result.paymentIntent.status === 'succeeded') {
                            // Change value of payment checker
                            $("#payment-checker").val("true");
                            // Submit form
                            form.submit();
                        }
                    }
                });
            // if posting fails
            }).fail(function () {
                // reload the page
                location.reload();
            });
        };
    });
});