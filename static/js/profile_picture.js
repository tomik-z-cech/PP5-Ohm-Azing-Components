$(document).ready(function() {
    let inputDiv = $("#id_profile_picture").closest("div");
    inputDiv.hide();
    $("#profile-picture-handler").click(function() {
        $("#id_profile_picture").click();
    });
    $("#id_profile_picture").change(function() {
        let file = this.files[0];
        if (file) {
            let reader = new FileReader();
            reader.onload = function(e) {
                $("#profile-picture-preview").css("display", "block");
                $("#initials").hide();
                $("#profile-picture-preview").attr("src", e.target.result);
            };
            reader.readAsDataURL(file);
        };
    });
});