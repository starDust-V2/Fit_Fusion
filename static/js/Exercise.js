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
			console.log(exercise_id)

			var exerciseCard = `<div class="exercise-card">
								<div class="name"><a href= 'individual_exercise?exercise_id=${exercise_id}+'>${exercise.name}</a></div>
								<div class="body-part"><span class="what-title"> Body-Part : &nbsp</span>${exercise.bodyPart}</div>
								<div class="equipment"><span class="what-title">Equipment : &nbsp</span>${exercise.equipment}</div>
								<div class="target"><span class="what-title">Target Muscle : &nbsp</span>${exercise.target}</div>
								<img src=${exercise.gifUrl} alt="">
								</div>` 


			document.querySelector(".main-content-inner").insertAdjacentHTML('beforeend', exerciseCard)
		 }

	} catch (error) {
		console.error(error);
	}
}






