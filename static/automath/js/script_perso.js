var questions = document.querySelectorAll("#questions > li");   // Sélectionne les questions
var reponses = document.getElementById("réponses");             // et les réponses

var i = 0;                  //  set your counter to 1
var stop = false;

	var num_questions = document.getElementsByClassName("numero_question");
	for (let j = 0; j < num_questions.length; j++) {
		num_questions[j].innerHTML = 'Question '+(j+1)+':'
	}

function myLoop() {         //  create a loop function
	questions[i].className = 'en_cours list-group-item list-group-item-success';
	var temps = document.getElementById("demo").innerHTML * 1000
	setTimeout(function () {   //  call a setTimeout when the loop is called
		questions[0].className = "masqué"
		if (i >= 1) {
			questions[i].className = 'masqué';
		}
		i++;                    //  increment the counter
		if (i < questions.length && stop === false) {           //  if the counter < 10, call the loop function
			myLoop();             //  ..  again which will trigger another
		} else { // Si fin des question ou bouton restart
			alert("Fin !");
			reponses.className = "affiché"
		}                    //  ..  setTimeout()
	}, temps)
}


var bouton_demarrer = document.getElementById("demarrer");
bouton_demarrer.addEventListener("click", myLoop)                //  start the loop


var bouton_restart = document.getElementById("restart");
bouton_restart.addEventListener("click", restart)                //  start the loop

function restart() {
	i = 0;
	stop = true;
	window.location.reload();
}

function affichageTemps(val) {
	document.getElementById("demo").innerHTML = val;
}