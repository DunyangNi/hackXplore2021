
var questionaire_score = 0;
var journal_entry = "";
var date = "";

function selectMCQ(event) {
	const target = event.target
	const value = target.value
	questionaire_score += parseInt(value)
	console.log(questionaire_score)
}

function submit() {
	var radio_buttons = document.getElementsByTagName("input")
	console.log(radio_buttons)
	for (i = 0; i < radio_buttons.length; i++) {
		radio_buttons[i].checked = false;
	}

	journal_entry = document.getElementById("journal_text").value
	var entry_box = document.getElementById("journal_text")
	entry_box.value = "";

	date = document.getElementById("date").value
	var date_element = document.getElementById("date")
	date_element.value = "";
	addEntry(questionaire_score, journal_entry, date)
	refresh()
}

function addEntry(score, entry, date) {
	const entries_container = document.getElementsByClassName("entries_container")

	const new_entry = document.createElement("div")
	new_entry.className = "entry"
	const entry_text = document.createElement("div")
	entry_text.className = "entry_text"

	const q_score = document.createElement("div")
	q_score.innerHTML = "Questionaire score: " + score

	const paragraph = document.createElement("p")
	paragraph.innerHTML = entry

	entry_text.appendChild(q_score)
	entry_text.appendChild(paragraph)

	const entry_date = document.createElement("div")
	entry_date.className = "entry_date"
	entry_date.innerHTML = "<span><i class='fas fa-calendar-week'></i></span> <b>" + date + "</b>"
	
	new_entry.appendChild(entry_date)
	new_entry.appendChild(entry_text)

	entries_container[0].prepend(new_entry)
}

function refresh(){
	questionaire_score = 0;
	journal_entry = "";
	date = "";
}

