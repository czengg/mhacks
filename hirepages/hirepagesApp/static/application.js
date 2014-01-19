function onLinkedInAuth() {
	IN.API.Profile("me").fields("positions","educations","skills").result(displayProfiles);
}

function displayProfiles(profiles) {
	var member = profiles.values[0];
	console.log(member.positions.values);

	var i = 0;
	member.positions.values.forEach(function(pos) {
		console.log(pos.title);
		console.log(pos.summary);
	}) 
}

function cloneMore(selector, type) {
    var newElement = $(selector).clone(true);
    var total = $('#id_' + type + '-TOTAL_FORMS').val();
    newElement.find(':input').each(function() {
        var name = $(this).attr('name').replace('-' + (total-1) + '-','-' + total + '-');
        var id = 'id_' + name;
        $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
    });
    newElement.find('label').each(function() {
        var newFor = $(this).attr('for').replace('-' + (total-1) + '-','-' + total + '-');
        $(this).attr('for', newFor);
    });
    total++;
    $('#id_' + type + '-TOTAL_FORMS').val(total);
    $(selector).after(newElement);
}

// EVENT HANDLERS

$(document).ready( function() {

	$("#experienceAdd").click(function() {
		cloneMore('div.experienceForm:last', 'form');
	})

	$(".experienceDelete").click(function() {
		console.log($('div.experienceForm:last'));
		$('div.experienceForm:last').remove();
		this.destroy();
	})

	$("#createPageButton").click(function() {
		$("#lookingForm").submit();
	})
})


