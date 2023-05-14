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
   else if (bookingType == "half-day") {
        // show only date input
        var dateInput = document.createElement("input");
        dateInput.type = "date";
        dateInput.id = "date";
        dateInput.required = true;

        // show slot select options
        var slotSelect = document.createElement('select');
        slotSelect.id = 'slot';
        slotSelect.required = true;
        var option = document.createElement('option');
        option.value = '';
        option.disabled = 'disabled';
        option.selected = 'selected';
        option.innerHTML = '-- Select Option --';
        var breakFastOption = document.createElement('option');
        breakFastOption.value = 'breakfast';
        breakFastOption.innerHTML = 'Breakfast';
        var lunchOption = document.createElement('option');
        lunchOption.value = 'lunch';
        lunchOption.innerHTML = 'Lunch';
        var dinnerOption = document.createElement('option');
        dinnerOption.value = 'dinner';
        dinnerOption.innerHTML = 'Dinner';

        slotSelect.appendChild(option);
        slotSelect.appendChild(breakFastOption);
        slotSelect.appendChild(lunchOption);
        slotSelect.appendChild(dinnerOption);

        document.getElementById("booking-options").appendChild(dateInput);
        document.getElementById("booking-options").appendChild(slotSelect);

    }
   else if (bookingType == "hourly") {
        // show only date input
        var dateInput = document.createElement("input");
        dateInput.type = "date";
        dateInput.id = "date";
        dateInput.required = true;

        // show Time input
        var timeInput = document.createElement("input");
        timeInput.type = "time";
        timeInput.id = "time";
        timeInput.required = true;

        document.getElementById("booking-options").appendChild(dateInput);
        document.getElementById("booking-options").appendChild(timeInput);
    }
}