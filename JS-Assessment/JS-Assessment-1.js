function showBookingOptions() {
    // remove previous booking options
    document.getElementById("booking-options").innerHTML = "";

    var bookingType = document.getElementById("booking-type").value;

    if (bookingType == "full-day") {
        // show only date input
        var dateInput = document.createElement("input");
        dateInput.type = "date";
        dateInput.id = "date";
        dateInput.required = true;
        document.getElementById("booking-options").appendChild(dateInput);
    }
}