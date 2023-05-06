async function api_call_all()
{
	const url = 'https://exercisedb.p.rapidapi.com/exercises';
	const options = {
		method: 'GET',
		headers: {
			'X-RapidAPI-Key': '0e4418edcemshb5469347fbe1173p1ced39jsn478c26435699',
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
		var exerciseCard = `<div class="exercise-card">
								<div class="name"><a href= 'individual_exercise?exercise_id=0662+'>push-up</a></div>
								<div class="body-part"><span class="what-title"> Body-Part : &nbsp</span>chest</div>
								<div class="equipment"><span class="what-title">Equipment : &nbsp</span>body weight</div>
								<div class="target"><span class="what-title">Target Muscle : &nbsp</span>pectorals</div>
								<img src='http://d205bpvrqc9yn1.cloudfront.net/0662.gif' alt="">
								</div>` 

			exerciseCard = exerciseCard + `<div class="exercise-card">
								<div class="name"><a href= 'individual_exercise?exercise_id=3222+'>semi squat jump (male)</a></div>
								<div class="body-part"><span class="what-title"> Body-Part : &nbsp</span>cardio</div>
								<div class="equipment"><span class="what-title">Equipment : &nbsp</span>body weight</div>
								<div class="target"><span class="what-title">Target Muscle : &nbsp</span>cardiovascular system</div>
								<img src='http://d205bpvrqc9yn1.cloudfront.net/3222.gif' alt="">
								</div>` 
	
			exerciseCard = exerciseCard + `<div class="exercise-card">
								<div class="name"><a href= 'individual_exercise?exercise_id=1670+'>dumbbell one arm standing curl</a></div>
								<div class="body-part"><span class="what-title"> Body-Part : &nbsp</span>upper arms</div>
								<div class="equipment"><span class="what-title">Equipment : &nbsp</span>dumbbell</div>
								<div class="target"><span class="what-title">Target Muscle : &nbsp</span>biceps	</div>
								<img src= 'http://d205bpvrqc9yn1.cloudfront.net/1670.gif' alt="">
								</div>`
			document.querySelector(".main-content-inner").insertAdjacentHTML('beforeend', exerciseCard);
			exerciseCard = "";
		// Loop through exercises and generate HTML dynamically
		 for (var i = 0; i < 100; i++) {
            var exercise = parsed_result[i];
			var exercise_id = exercise.id;
			console.log(exercise_id);

	

			exerciseCard = `<div class="exercise-card">
								<div class="name"><a href= 'individual_exercise?exercise_id=${exercise_id}+'>${exercise.name}</a></div>
								<div class="body-part"><span class="what-title"> Body-Part : &nbsp</span>${exercise.bodyPart}</div>
								<div class="equipment"><span class="what-title">Equipment : &nbsp</span>${exercise.equipment}</div>
								<div class="target"><span class="what-title">Target Muscle : &nbsp</span>${exercise.target}</div>
								<img src=${exercise.gifUrl} alt="">
								</div>` 


			document.querySelector(".main-content-inner").insertAdjacentHTML('beforeend', exerciseCard);
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
            'X-RapidAPI-Key': '0e4418edcemshb5469347fbe1173p1ced39jsn478c26435699',
            'X-RapidAPI-Host': 'exercisedb.p.rapidapi.com'
        }
    };

    try {
        const response = await fetch(url, options);
        const result = await response.text();
        let parsed_result = JSON.parse(result);
        let exercise= parsed_result;

        var exerciseCard = `<div class="exercise-card individual">
								<div class="name"><a href= 'individual_exercise?exercise_id=${exercise_id}+'>${exercise.name}</a></div>
								<div class="body-part"><span class="what-title"> Body-Part : &nbsp</span>${exercise.bodyPart}</div>
								<div class="equipment"><span class="what-title">Equipment : &nbsp</span>${exercise.equipment}</div>
								<div class="target"><span class="what-title">Target Muscle : &nbsp</span>${exercise.target}</div>
								<img src=${exercise.gifUrl} alt="">
								</div>` 


			document.querySelector(".main-content-inner").insertAdjacentHTML('beforeend', exerciseCard);

			

    } catch (error) {
        console.error(error);
    }
}






