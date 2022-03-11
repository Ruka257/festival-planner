# QA Ltd DevOps DfE digital skills bootcamp, March 2022: Final project

<h3>DfE Project Scope</h3>
<p>The scope of this project requires the trainee DevOps engineer to design and programme a simple object-oriented Python Flask app with HTML templates that integrates with a structured database. The database should exhibit Create, Read, Update, and Delete (CRUD) functionality. Unit tests should test for integration as well as CRUD functionality. Once created, the app should be built automatically using a Jenkins pipeline script in the Jenkins automation server. Once successful, the app will deployed in a cloud-native development environment using Docker. Once the app image is built, it will run as a docker container with attributes gleanedd from the app's associated Dockerfile. Should this succed and the database data persist, it will be ready for multi-node deployment with Docker Swarm.</p>
<h3>Planning Stage</h3>
<strong>How does the project work?</strong>
<p>This project consists of a Flask webapp designed to allow users to create a list of festivals they wish to attend, and add acts to the festival lineup in different timeslots.</p>
<p>A series of epics were written on Jira consisting of user stories for the app user as well as the DevOps engineer over the course of <a href="https://rebekah-akingbala.atlassian.net/jira/software/projects/QBAFA/boards/2/roadmap">two sprints</a>. Jira progress updates, comments, and task assignment were integrated into a number of <a href="https://rebekah-akingbala.atlassian.net/jira/software/projects/QBAFA/code">Ruka257 GitHub Repos</a> using Smart Commits. Second sprint with larger team and more brainstorming, cross collaboration would allow for story points assigned after unanimous ‘planning poker’ result at daily standups.</p>
<p>Credentials for meeting the definition of done were scaled back due to the initial sprint taking place over one week rather than two weeks. Linked issues that were blocked by the inability to create a functional MySQL db slowed progress. A <a href="https://docs.google.com/spreadsheets/d/1A8KUrp5BsRaqJweXAlm7HBaXc4gdpwFKgeboT5DccEA/edit?usp=sharing">risk assessment matrix</a> was created to anticipate and acknowledge setbacks during the project. Entries in row 5 attest to the difficulties in creating a working MySQL script in this project. MySQL is suitable for the scope of this project being undertaken by a single user, or when scaled, a small-to-medium sized business. An Enterprise however, would have much more complex relationships between their entities such as many-to-many, which could not be modelled in MySQL without a join table between the two main entity tables. Instead, this app uses a Flask sqlite database instead (db) with efforts made to meet CRUD functionality necesscary for the Minimum Viable Product (MVP). My Entity Relationship Diagram (ERD) for the two tables in the db can be found <a href="https://drive.google.com/file/d/1AAGMHl3QwkLKCghRbad20MXuhN5mQizZ/view?usp=sharing">here.</a>
<br> In a third sprint, the database this app uses could model a many-to-many relationship, with an additional join table for multiple stages that acts can perform on at any given festival.</p>
<h3>Development Stage</h3>
<p>This <a href="https://drive.google.com/file/d/10QPw0NZEc1ZL586dcJxjbUwb6EpJKZXZ/view?usp=sharing">diagram</a> details the tech stack necesscary for the effective deployment of the festival app's MVP. Incorrect workflow meant the app code on the initial GitHub project repo <a href="https://drive.google.com/file/d/1k673GmtWV_x2AGKxbjH0ZJ6guPagAKMM/view?usp=sharing">could not be pulled from the local machine.</a> In an attempt to mitigate against the issue specified in <a href="https://docs.google.com/spreadsheets/d/1A8KUrp5BsRaqJweXAlm7HBaXc4gdpwFKgeboT5DccEA/edit#gid=0&range=F16">cell 16F of the risk assessment,</a> a new repo was created (this repo) with a ‘development’ branch in order to host code during the development and testing phasee, prior to staging and deployment. In an enterprise environment, a new feature branch for each directory of the working app code should be created in order to minimise conflicts betwwen developers, and for easier bug tracking. A dev team member could look at the ‘merge pull' request and unit test the code before merging it into the development branch. Multiple feature branches were outside the scope of this project given the short sprint time and only having one contributor, so only a ‘main’ branch for deployment-ready code and a ‘development’ branch for code in production and awaiting testing were used.</p><br>
<p>To advance the project's progress, a simple web app was pulled from <a href="https://github.com/Ruka257/qa-flask-week/blob/main/flask-unit-testing/app.py">another Ruka257 repo</a> in order to write simple unit tests and move on to the development VM. Edits were made in <a href="https://drive.google.com/file/d/10QPw0NZEc1ZL586dcJxjbUwb6EpJKZXZ/view?usp=sharing"> Visual Studio Code</a>to remove sensitive and unecesscary data such as the db URI string, cached files and the virtual environment (venv) from the repo. The internal flask db was used to run the tests by exporting the db URI in the terminal session to improve security.<a href="https://drive.google.com/file/d/1Ux8BSQUJLjRsivSs05doVbWewNAgitWW/view?usp=sharing">The unit test script for create functionality was then written and executed here.</a> The image shows a successful test for create functionality with 100% coverage, however the init.py shows zero statements as the code was moved into a single app.py file in order to adher to the Don't Repeat Yourself (DRY) coding principle and reduce the app's memory while maintaining the same capabilities. Unfortunately, <a href="https://drive.google.com/file/d/16UfpDeGrtllHY1BAekUD04oWYcHelnDW/view?usp=sharing">the development VM's terminal froze, disconnected and broke down before the tests could be committed</a> and replicated in the festival app repo. The changes and test report weren’t pushed to github due to a terminal connection error on the VM <a href="https://drive.google.com/file/d/1BhTUXrQsgj1qStu2_djyK8mwpWryPfye/view?usp=sharing"> which prevented the VM from being restarted, stopped, or deleted until the following day</a>. This VM was deleted in order to create a jenkins pipeline for the app using a basic test script. Once the app was built successfully, I went back and wrote unit tests for the script to test CRUD functionality and attempted a preliminary paramertised build of the app through Jenkins on my new VM.</p>
<p>The builds were successful but turned out to show false positives. The initial export of the db URI in the terminal <a href="https://drive.google.com/file/d/10WT6GIxOKe074GNIlRITRvV4PbUVh_V3/view?usp=sharing">duplicated the environment variable (ENV) set up in the build parameters</a>. In the second build, the VM <a href="https://drive.google.com/file/d/1Vmp7FoxWMUs8GIcwldBtWPu40tOzpWcg/view?usp=sharing">did not have the Flask module installed from pip</a> so the app didn't build despite the script code running successfully. Further build attempts using Jenkins were shared with the project assessor via video.</p>
<p>A larger DevOps team and a usual sprint time of 2 weeks would be a significant driver in successfully deploying the festival app. The Dockerfile contains details of the necesscary layers to build an image from which the app can be deployed simultaneously in the cloud on various nodes using dockerswarm.</p>