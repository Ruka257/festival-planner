# QA Ltd DevOps DfE digital skills bootcamp, March 2022: Final project

<h3>DfE Project Scope</h3>
<p>The scope of this project requires the trainee DevOps engineer to design and programme a simple object-oriented Python Flask app with HTML templates that integrates with a structured database. The database should exhibit Create, Read, Update, and Delete (CRUD) functionality. Unit tests should test for integration as well as CRUD functionality. Once created, the app should be built automatically using a Jenkins pipeline script in the Jenkins automation server. Once successful, the app will deployed in a cloud-native development environment using Docker. Once the app image is built, it will run as a docker container with attributes gleanedd from the app's associated Dockerfile. Should this succed and the database data persist, it will be ready for multi-node deployment with Docker Swarm.</p>

<h3>What this project does</h3>
<p>This project consists of a Flask webapp designed to allow users to create a list of festivals they wish to attend, and add acts to the festival lineup in different timeslots.</p>
<p><strong>How does the project work?</strong>

<p>A series of epics were written on Jira consisting of user stories for the app user as well as the DevOps engineer over the course of <a href="https://rebekah-akingbala.atlassian.net/jira/software/projects/QBAFA/boards/2/roadmap">two sprints</a>. Jira progress updates, comments, and task assignment were integrated into a number of <a href="https://rebekah-akingbala.atlassian.net/jira/software/projects/QBAFA/code">Ruka257 GitHub Repos</a> using Smart Commits.</p>
<p>Credentials for meeting the definition of done were scaled back due to the initial sprint taking place over one week rather than two weeks. Linked issues that were blocked by the inability to create a functional MySQL db slowed progress. A <a href="https://docs.google.com/spreadsheets/d/1A8KUrp5BsRaqJweXAlm7HBaXc4gdpwFKgeboT5DccEA/edit?usp=sharing">risk assessment matrix</a> was created to anticipate and acknowledge setbacks during the project. Entries in row 5 attest to the difficulties in creating a working MySQL script in this project.</p>
Instead, this app uses a Flask sqlite database instead (db) with efforts made to meet CRUD functionality necesscary for the Minimum Viable Product (MVP). My Entity Relationship Diagram (ERD) for the two tables in the db can be found <a href="https://drive.google.com/file/d/1AAGMHl3QwkLKCghRbad20MXuhN5mQizZ/view?usp=sharing">here.</a>
<br> In a third sprint, the database this app uses could model a many-to-many relationship, with an additional join table for multiple stages that acts can perform on at any given festival.</p>
<p>Created a new project repo and checked out a ‘development’ branch in order to host my code in the development stage, prior to staging/testing, and deployment. In an enterprise environment I would have created a new feature branch for each branch of my app. A dev team member could look at the ‘merge pull request’ and test the code changes with unit tests for example, before merging with the development branch. Multiple feature branches were outside the scope of my project given the short sprint time and only having one contributor, so only a ‘main’ branch for deployment-ready code and a ‘development’ for code in production and awaiting tests were used.</p>

Incorrect workflow meant I couldn't push my <a href="https://drive.google.com/file/d/1k673GmtWV_x2AGKxbjH0ZJ6guPagAKMM/view?usp=sharing">initial repo code up to development branch from my local machine.</a>