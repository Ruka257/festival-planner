# QA Ltd DevOps DfE digital skills bootcamp, March 2022: Final project

<h3>DfE Project Scope</h3>
<p>The scope of this project requires the trainee DevOps engineer to design and programme a simple object-oriented Python Flask app with HTML templates that integrates with a structured database. The database should exhibit Create, Read, Update, and Delete (CRUD) functionality. Unit tests should test for integration as well as CRUD functionality. Once created, the app should be built automatically using a Jenkins pipeline script in the Jenkins automation server. Once successful, the app will deployed in a cloud-native development environment using Docker. Once the app image is built, it will run as a docker container with attributes gleanedd from the app's associated Dockerfile. Should this succed and the database data persist, it will be ready for multi-node deployment with Docker Swarm.</p>
<br>
<h3>What this project does</h3>
<p>This project consists of a Flask webapp designed to allow users to create a list of festivals they wish to attend, and add acts to the festival lineup in different timeslots.</p>
<p><strong>How does the project work?</strong>

<p>A series of epics were written on Jira consisting of user stories for the app user as well as the DevOps engineer over the course of <a href="https://rebekah-akingbala.atlassian.net/jira/software/projects/QBAFA/boards/2/roadmap">two sprints</a>. Jira progress updates, comments, and task assignment were integrated into a number of <a href="https://rebekah-akingbala.atlassian.net/jira/software/projects/QBAFA/code">Ruka257 GitHub Repos</a> using Smart Commits.</p>
<p>Credentials for meeting the definition of done were scaled back due to the initial sprint taking place over one week rather than two weeks. Linked issues that were blocked by the inability to create a functional MySQL db slowed progress.

A <a href=”QA Project Risk Assessment”>risk assessment matrix</a> was for potential setbacks during the project.
This app uses a Flask sqlite database (db) with CRUD functionality. My Entity Relationship Diagram (ERD) for the two tables in the db can be found <a href="https://drive.google.com/file/d/1AAGMHl3QwkLKCghRbad20MXuhN5mQizZ/view?usp=sharing">here.</a></p>

<strong>Who is the project useful for?</strong> 

<strong>How can you get started with the project?</strong>  Set-up the site and write down exact instructions

<strong>Where can users get help with the project?</strong>:

<strong>Who maintains and contributes to the project?</strong>:
# festival-planner
