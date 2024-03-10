// Common Passwords to compare
let tooCommonPass = [
    "password",
    "123456",
    "123456789",
    "qwerty",
    "abc123",
    "111111",
    "123123",
    "admin",
    "letmein",
    "welcome",
    "monkey",
    "1234",
    "12345",
    "1234567",
    "12345678",
    "1234567890",
    "password1",
    "123",
    "1234",
    "12345",
    "123456",
    "1234567",
    "12345678",
    "123456789",
    "1234567890",
    "qwertyuiop",
    "asdfghjkl",
    "zxcvbnm",
    "123qwe",
    "123abc"
];

// Checkers of 4 password conditions
let passOK1 = false;
let passOK2 = false;
let passOK3 = false;
let passOK4 = false;

$(document).ready(function () {
    // Initially hide register button
    $(".register-submit-item").css("opacity", "0").css("pointer-events", "none");
    // If any registration fields change
    $("#id_password1, #id_password2, #id_email, #id_email2, #id_username").on("input", function() {
        // If pasword empty change color to white of all conditions
        if ($("#id_password1").val().length < 1){
            $(".register-submit-item").css("opacity", "0").css("pointer-events", "none");
            $(".form-background ul li:nth-child(1)").css("color", "var(--light-foreground)");
            $(".form-background ul li:nth-child(2)").css("color", "var(--light-foreground)");
            $(".form-background ul li:nth-child(3)").css("color", "var(--light-foreground)");
            $(".form-background ul li:nth-child(4)").css("color", "var(--light-foreground)");
        } else {
            // If password longer then 8 characters
            if ($("#id_password1").val().length > 8) {
                // Highlight condition passed and set checker
                $(".form-background ul li:nth-child(2)").css("color", "var(--light-highlight)");
                passOK1 = true;
            } else {
                // Make condition not highlighted and unset checker
                $(".form-background ul li:nth-child(2)").css("color", "var(--light-foreground)");
                passOK1 = false;
            }
            // If password contains at least one letter
            if (/[a-zA-Z]/.test($("#id_password1").val())) {
                // Highlight condition passed and set checker
                $(".form-background ul li:nth-child(4)").css("color", "var(--light-highlight)");
                passOK2 = true;
            } else {
                // Make condition not highlighted and unset checker
                $(".form-background ul li:nth-child(4)").css("color", "var(--light-foreground)");
                passOK2 = false;
            }
            // If username not included in password
            if ($("#id_password1").val().toLowerCase().includes($("#id_username").val().toLowerCase()) && $("#id_username").val().length > 0 ) {
                // Make condition not highlighted and unset checker
                $(".form-background ul li:nth-child(1)").css("color", "var(--light-foreground)");
                passOK3 = false;
            } else {
                // Highlight condition passed and set checker
                $(".form-background ul li:nth-child(1)").css("color", "var(--light-highlight)");
                passOK3 = true;
            }
            // If passsword not included in common passwords above
            if (tooCommonPass.includes($("#id_password1").val().toLowerCase())) {
                // Make condition not highlighted and unset checker
                $(".form-background ul li:nth-child(3)").css("color", "var(--light-foreground)");
                passOK4 = false;
            } else {
                // Highlight condition passed and set checker
                $(".form-background ul li:nth-child(3)").css("color", "var(--light-highlight)");
                passOK4 = true;
            }
        }
        // All 4 conditions are true and other fields are not empty
        if (passOK1 == true && passOK1 == true && passOK1 == true && passOK1 == true && $("#id_username").val().length > 0 && $("#id_email").val().length > 0 && $("#id_email2").val().length > 0 && $("#id_password2").val().length > 0 && $("#id_password2").val() == $("#id_password1").val()){
            // Show register buttton
            $(".register-submit-item").css("opacity", "1").css("pointer-events", "auto");
        } else {
            // Hide regisater button
            $(".register-submit-item").css("opacity", "0").css("pointer-events", "none");
        }
    });
});