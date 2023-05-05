async function api_call_all()
{
	const url = 'https://exercisedb.p.rapidapi.com/exercises';
	const options = {
		method: 'GET',
		headers: {
			'X-RapidAPI-Key': 'c56e9a8e6emshb21b889df59c1f3p1325f2jsn828ee3b47f1e',
			'X-RapidAPI-Host': 'exercisedb.p.rapidapi.com'
		}
	};

	try {
		const response = await fetch(url, options);
		const result = await response.text();
		let parsed_result = JSON.parse(result);
		console.log(typeof(result));

		console.log(parsed_result[0]);
		console.log(parsed_result[0].name);
		
		//displaying all the exercise:
		// Loop through exercises and generate HTML dynamically
		 for (var i = 0; i < parsed_result.length; i++) {
            var exercise = parsed_result[i];
			var exercise_id = exercise.id;
			var html = "<div> <a href= 'individual_exercise?exercise_id="+exercise_id+"'>";
            html += "<div class='exercise-card'>";
            html += "<h1>Exercise Details</h1>";
            html += "<p><strong>Name:</strong> " + exercise.name + "</p>";
            html += "<p><strong>Body Part:</strong> " + exercise.bodyPart + "</p>";
            html += "<p><strong>Equipment:</strong> " + exercise.equipment + "</p>";
            html += "<p><strong>Target:</strong> " + exercise.target + "</p>";
            html += "<img src='" + exercise.gifUrl + "' alt='Exercise GIF'>";
            html += "</div></a></div>";
            document.write(html);
		 }

	} catch (error) {
		console.error(error);
	}
}




async function api_call_individual()
{
	//get variable value from url:
	const urlParams = new URLSearchParams(window.location.search);
	const exercise_id = urlParams.get('exercise_id');

	const url = 'https://exercisedb.p.rapidapi.com/exercises/exercise/'+ exercise_id ;
	console.log(url);
	const options = {
		method: 'GET',
		headers: {
			'X-RapidAPI-Key': 'c56e9a8e6emshb21b889df59c1f3p1325f2jsn828ee3b47f1e',
			'X-RapidAPI-Host': 'exercisedb.p.rapidapi.com'
		}
	};

	try {
		const response = await fetch(url, options);
		const result = await response.text();
		let parsed_result = JSON.parse(result);
		let exercise= parsed_result;
		
        var html = "<div class='exercise-card'>";
            html += "<h1>Exercise Details</h1>";
            html += "<p><strong>Name:</strong> " + exercise.name + "</p>";
            html += "<p><strong>Body Part:</strong> " + exercise.bodyPart + "</p>";
            html += "<p><strong>Equipment:</strong> " + exercise.equipment + "</p>";
            html += "<p><strong>Target:</strong> " + exercise.target + "</p>";
            html += "<img src='" + exercise.gifUrl + "' alt='Exercise GIF'>";
            html += "</div>";
		
		document.getElementById('main_div').innerHTML= html;

	} catch (error) {
		console.error(error);
	}
}



