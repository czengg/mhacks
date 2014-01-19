function onLinkedInAuth() {
	IN.API.Profile("me").fields("positions").result(displayProfiles);
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