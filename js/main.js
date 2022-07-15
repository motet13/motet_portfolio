let projectList = [];
// Project Object
function Project(title, description, detail, image, btn) {
	this.title = title;
	this.description = description;
	this.detail = detail;
	this.image = image;
	this.btn = btn;

	projectList.push(this);
}

Project.prototype.make = function() {
		// variable for appending newly created elements here.
		let projConPosition = document.getElementById('my-work');
		
		// first create a div element with a class of project-container.
		let projectContainer = document.createElement('div');
		projectContainer.className = 'project-container';

		// second, create inner div with a class of project and shadow-lower that will go inside .project-container.
		let project = document.createElement('div');
		project.classList.add('project', 'shadow-lower');

		// create and add img, h2, p(2x), a elements into .project
		// create img element
		let img = document.createElement('img');
		img.src = this.image;

		// create h2 element
		let projectTitle = document.createElement('h2');
		let titleNode = document.createTextNode(this.title);
		projectTitle.appendChild(titleNode);

		// create two p elements
		let projectDesc = document.createElement('p');
		let descNode = document.createTextNode(this.description);
		projectDesc.appendChild(descNode);

		let projectDetail = document.createElement('p');
		let detailNode = document.createTextNode(this.detail);
		projectDetail.appendChild(detailNode);

 		// create a element
		let projectBtn = document.createElement('a');
		let btnNode = document.createTextNode('see more');
		projectBtn.setAttribute('href', '#');
		projectBtn.className = 'button';
		projectBtn.appendChild(btnNode);

 		// Append all newly created elements and show them in the browser.
		projConPosition.appendChild(projectContainer);
		projectContainer.appendChild(project);
		project.appendChild(img);
		project.appendChild(projectTitle);
		project.appendChild(projectDesc);
		// project.appendChild(projectDetail);
		project.appendChild(projectBtn);
}

// Create instances of a class Project
// Add new projects here to update your work section page.

let morsecode = new Project(
	'Morse Code',
	'cipher & decipher morse code.',
	'a cli morse code program.',
	'images/place_image300x150.jpg',
	'#'
	);

for (var i = 0; i < projectList.length; i++) {
	projectList[i].make();
}