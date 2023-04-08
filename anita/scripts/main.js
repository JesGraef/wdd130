//Hamburger
// Store the selected elements that we are going to use. 
const mainnav = document.querySelector('.navigation')
const hambutton = document.querySelector('#menu');

// Add a click event listender to the hamburger button and use a callback function that toggles the list element's list of classes.
hambutton.addEventListener('click', () => {
	mainnav.classList.toggle('show');
	hambutton.classList.toggle('show');
});


// Site Last Updated
const date = new Date(document.lastModified);
const shortDate = date.toLocaleDateString('en-US');
document.getElementById("modified").innerHTML = shortDate;


// Hidden element on Join Page
// const today = new Date();
// document.querySelector('#dateTime').value = today;

