function onLinkedInAuth() {
	IN.API.Profile("me").fields("positions","educations","skills").result(displayProfiles);
}

function displayProfiles(profiles) {
	var member = profiles.values[0];

	$("#id_school").val(member.educations.values[0].schoolName);
	$("#id_major").val(member.educations.values[0].fieldOfStudy);

	window.ind = 0;
	member.positions.values.forEach(function(pos) {

		var id = "id_form-" + ind + "-";
		$("#" + id + "position").val(pos.title);
		$("#" + id + "company").val(pos.company.name);
		console.log(pos.summary);
		$("#" + id + "description").val(pos.summary);

		// $("#" + id + "startDate").val(pos.startDate.month + " " + pos.startDate.year);
		// $("#" + id + "endDate").val(pos.endDate.month + " " + pos.endDate.year);

		$("#experienceAdd").trigger("click");
		ind ++;
	})
}

// EVENT HANDLERS

$(document).ready( function() {

	// Code adapted from http://djangosnippets.org/snippets/1389/  
    function updateElementIndex(el, prefix, ndx) {
        var id_regex = new RegExp('(' + prefix + '-\\d+-)');
        var replacement = prefix + '-' + ndx + '-';
        if ($(el).attr("for")) {$(el).attr("for", $(el).attr("for").replace(id_regex,
        replacement))};
        if ($(el).context.id) {el.id = el.id.replace(id_regex, replacement)};
        if ($(el).context.name) {el.name = el.name.replace(id_regex, replacement)};
        // console.log(ndx)
    }

    function deleteForm(btn, prefix) {
        var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
        if (formCount > 1) {
            // Delete the item/form
            $(btn).parents('.experienceFormset').remove();
            var forms = $('.experienceFormset'); // Get all the forms  
            // Update the total number of forms (1 less than before)
            $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
            var i = 0;
            // Go through the forms and set their indices, names and IDs
            for (formCount = forms.length; i < formCount; i++) {
                $(forms.get(i)).children().children().each(function () {
                    if ($(this).attr('type') == 'text') updateElementIndex(this, prefix, i);
                });
            }
        } // End if
        else {
            alert("You have to enter at least one experience item!");
        }
        return false;
    }

    function addForm(btn, prefix) {
        var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());

        // You can only submit a maximum of 10 todo items 
        // Clone a form (without event handlers) from the first form
        var row = $(".experienceFormset:first").clone(false).get(0);
        // Insert it after the last form
        $(row).removeAttr('id').hide().insertAfter(".experienceFormset:last").slideDown(300);

        // Remove the bits we don't want in the new row/form
        // e.g. error messages
        $(".errorlist", row).remove();
        $(row).children().removeClass("error");

        window.co = formCount;

        // Relabel or rename all the relevant bits
        $(row).children().children(".experienceFields").children().each(function() {
            updateElementIndex(this, prefix, window.co);
            $(this).val("");
        });

        // Add an event handler for the delete item/form link 
        $(row).find(".experienceDelete").click(function () {
            return deleteForm(this, prefix);
        });
        // Update the total form count
        $("#id_" + prefix + "-TOTAL_FORMS").val(formCount + 1);
        return false;
    }
    // Register the click event handlers
    $("#experienceAdd").click(function () {
        return addForm(this, "form");
    });

    $(".experienceDelete").click(function () {
        return deleteForm(this, "form");
    });

	$("#createPageButton").click(function() {
		$("#lookingForm").submit();
	})

	$(".start_date").datepicker();
	$(".end_date").datepicker();
})


