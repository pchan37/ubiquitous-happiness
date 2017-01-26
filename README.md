# Lost & Found

### Team **PACK**: **P**atrick Chan, **A**yman Ahmed, **C**eline Yan, **K**evin Zhang

**Description**

*Lost & Found* is a website that seeks to reunite lost pets with their owners. It does so by facilitating contact between pet finders and pet owners. If a person has lost his/her pet, he/she can peruse our database for a possible match. If no matches are found, then the person can enter his pet into the database, in hopes that another person is able to find the pet. Likewise, a person who has found a pet can also peruse the database, in hopes of returning the pet to its rightful owner. If a match is found, the two people are given each others' contact information in order to open communication between the two.

**Instructions**

[Instructional Video]: https://www.google.com/	"Instructional Video"

1. Begin by running `python app.py` in the terminal. Go to the url `127.0.0.1:5000/` in your browser to get to the homepage
2. Decide whether you have found a pet, or lost a pet. Pick the appropriate option on the homepage
3. Fill out as much of the form on the top of the screen as possible in order to narrow results. The results should be displayed below. You may submit the form if none of the pets below match what you are looking for. If a pet matches what you are looking for however, you can click on the link below the pet to go to its pet page for more details
4. On the pet page, if the pet matches what you are looking for, you can claim it by clicking on the button on the bottom of your screen. This will copy the other person's contact info to your clipboard. If it does not match, however, you can return to the previous form page.
5. If you are unsuccessful in finding a pet that matches your specifications, you can add your pet to the database by pressing the submit button. That will take you to another page, where you are asked to confirm the details of your pet, as well as insert additional details. If you have a photo ready, uploading it would definitely be beneficial.
6. Once you submit that. you will be returned to the homepage. Feel free to go through the whole process again. 

**Additional Details**

Known Bugs:

- Going back from ```/pet/``` to ```/lost/``` or ```/found/``` clears out the previous form

Changes to Design:

- Added a separate table for pet information. Since this data ( petName, location, etc. ) is shared by both ListOfPetsLost and ListOfPetsFound, we split it off, and linked the tables through the use of a new entry ( petID ).
- Added an additional page ( confirm.html ), which allows the user to add personal details in addition to the form details filled out on the page prior. 
- Included image uploading for if the user wants to upload images.

<hr>

<div style="text-align: center">
think this project isnt important? well look at this happy corg after he was found using our project

<img src="https://s3.amazonaws.com/cms-uploads.adoptapet.com/e/4/d/5.png" alt="corgo" />
</div>

<hr>

