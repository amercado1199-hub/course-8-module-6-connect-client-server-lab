// Fetch all events from the Flask backend when the page loads
fetch("http://localhost:5000/events")
.then((response) => response.json())
.then((events) => {
// Display each event on the page
events.forEach(renderEvent);
});

// Listen for the form submission
document.querySelector("form").addEventListener("submit", (e) => {
// Stop the page from refreshing
e.preventDefault();

// Get the value typed into the input
const title = document.querySelector("#title").value;

// Send the new event to the Flask backend
fetch("http://localhost:5000/events", {
method: "POST",
headers: {
"Content-Type": "application/json",
},
body: JSON.stringify({ title }),
})
.then((response) => response.json())
.then((event) => {
// Add the new event to the page
renderEvent(event);
});
});

// Function that adds one event to the page
function renderEvent(event) {
const li = document.createElement("li");

// Set the list item text to the event title
li.textContent = event.title;

// Add the event to the event list
document.querySelector("#event-list").appendChild(li);
}
