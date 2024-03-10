$(document).ready(function() {
    // Set variable of the div of profile picture file input
    let inputDiv = $("#id_profile_picture").closest("div");
    // Hide the file input
    inputDiv.hide();
    // When the pseudo input clicked, open actual file input
    $("#profile-picture-handler").click(function() {
        $("#id_profile_picture").click();
    });
    // If the file picture changes
    $("#id_profile_picture").change(function() {
        // Set variable of file details
        let file = this.files[0];
        // If file uploaded correctly
        if (file) {
            // Set file reader
            let reader = new FileReader();
            // Once the reader loaded
            reader.onload = function(e) {
                // Display the containers correctly
                $("#profile-picture-preview").css("display", "block");
                $("#initials").hide();
                $("#profile-picture-preview").attr("src", e.target.result);
            };
            reader.readAsDataURL(file);
        }
    });
});