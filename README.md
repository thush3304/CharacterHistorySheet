# CharacterHistorySheet

## Introduction

### Aims
The aims for this project are:
> To create a service-orientated architecture for your application, this application must be composed of at least 4 services that work together.

For me this means:
1. Create 4 services that utilise one another to give a desired outcome.
2. Use Jenkins, Docker and Ansible to deploy the application.

The technologies that needed to be utilised were as follows:
* Version Control: Git - using the feature-branch model
* CI Server: Jenkins
* Configuration Management: Ansible
* Cloud server: GCP virtual machines
* Containerisation: Docker
* Orchestration Tool: Docker Swarm
* Reverse Proxy: NGINX
* Database Layer: MySQL


### My Idea
I have decided to create an application for which will take a random era alongisde a random title e.g. General and return a result based on these two alongside a factoid.

#### Character Display
* Service-1 (front-end): Displays the results of the following 3 services.
* Service-2: Returns a random Era from a list.
* Service-3: Returns a random Title from a list.
* Service-4: Returns a character from the period in time with a factoid.

### Architecture
#### Risk Assessment
My risk assessment can be seen below, outlining risks that have potential to impact the project. This helps me identify and come up with preventions for the potential risks.
![image](https://user-images.githubusercontent.com/86304577/129502324-e0b7b3c7-d8d8-414d-abf6-61a6bc696d2a.png)

#### Kanban Board
For project tracking I had decided to use Trello, as to previous experience where I had used JIRA it is a lot more lightweight and easier to use especially for individual projects.
![image](https://user-images.githubusercontent.com/86304577/129502850-33fe433a-4403-41c9-a0c5-526957c51e83.png)

#### Analysis of Testing
This project requires utilising testing to its full in order to make sure that all parts of the CI/CD pipeline are running smoothly and work efficiently.
![image](https://user-images.githubusercontent.com/86304577/129502975-22dd8e07-4ac8-47f3-bb6e-9f20823c5c69.png)

### Infrastructure

In this project I have attempted to implement a Continous Deployment structure so that new versions of the application can be deployed quickly with limited down time.

#### Jenkins
I have used webhook feature in GitHub to create a webhook with Jenkins which will get triggered and updated on each push. Upon each push it will go through scripts to execute the following:

Initially this is implemented to install dependencies and get a coverage report:
> sudo apt-get update > /dev/null
> sudo apt-get install python3 python3-venv libpq-dev -y > /dev/null
>
> #Install pip requirements
> python3 -m venv venv && source venv/bin/activate
> pip3 install --upgrade pip
> pip3 install --upgrade setuptools
> for i in {1..4}; do 
> pip3 install -r service_${i}/requirements.txt > /dev/null; 
> done 
> 
> #Unit testing
> python3 -m pytest --disable-warnings --cov --cov-config=.coveragerc --cov-report=term-missing

After which:
##### Build & Push: docker-compose
> Jenkins' credentials system is used to log in to Docker Hub, where the new images are then pushed into the specific repository.

##### Ansible
>Ansible configures several things:

> 1.Installing dependencies,
> 2.Setting up the swarm, and joining the swarm on all worker nodes.

##### Deploy: docker swarm/stack
> Jenkins copies the docker-compose.yaml file on to the manager node,and runs docker stack deploy. The script for which is shown below and in the JenkinsFile:

> pipeline{
>    agent any
> 
>     environment{
>         DOCKERHUB = credentials('DOCKERHUB')
>         DATABASE_URI = credentials('DATABASE_URI')
>         MYSQL_ROOT_PASSWORD = credentials('MYSQL_ROOT_PASSWORD')
>     }
> 
>     stages{
>         stage('Install Dependencies'){
>             steps{
>                 sh "bash scripts/setup.sh"
>             }
>         }
> 
>         stage('Run Unit Tests'){
>             steps{
>                 sh "bash scripts/test.sh"
>             }
>         }
> 
>         stage('Build And Push Docker Images'){
>             steps{
>                 sh "bash scripts/build.sh"
>             }
>         }
> 
>         stage('Configure Hosts For Deployment'){
>             steps{
>                 sh "bash scripts/config.sh"
>             }
>         }
> 
>         stage('Deploy Stack Manager'){
>             steps{
>                 sh "bash scripts/deploy.sh"
>             }
>         }
>     }
> }
#### Pipeline Diagram:
![image](https://user-images.githubusercontent.com/86304577/129504677-9bc12101-b535-4a66-bd73-696d30e9a0c4.png)
Above is the final pipeline that is to be acheived through this project as shown much of the process is automated and is very smooth and fast due to the technologies involved. Below is the initial pipeline utilised which is very basic and utilises only Jenkins. This is very slow and has no load balancing and has increased downtime for updates.
![image](https://user-images.githubusercontent.com/86304577/129504695-4db514d7-f2a9-4185-b88b-38bc41de4367.png)

#### Entity Diagram:
This project only uses one table in the database however it is still important to detail the structure of the table. Below is a diagram for the table used in this project.
![image](https://user-images.githubusercontent.com/86304577/129505171-c10f6136-5719-43a0-bfe9-4428c9976c51.png)
On the right is the initial ERD that I had developed for this project as you can see the set theme is the same however the data variables are not. The reason why this struture was not followed through with was due to the fact that this system would have meant I would be posting to both service 3 and 4 rather than just service 4. Rather than making the task harder for myself I opted for the second ERD which proved to be easier to implement as an application.

#### Interactions Diagram:
![image](https://user-images.githubusercontent.com/86304577/129505875-7c1e2de0-52f9-4e3a-9d21-fea6821eaa40.png)
Using Docker Swarm, I created a virtual machine network which can be accessed by the user. As the diagram shows, this network includes NGINX load-balancer which diverts the user to a VM that has the least connections.

#### 4 Services:
![image](https://user-images.githubusercontent.com/86304577/129508943-8aa93164-4d24-44a1-8249-d36993c0c9c3.png)

How this system works is the front-end sends GET requests to service1 and 2. This then sends the response to service 3 as a POST request, and service 3 sends its data to service 1. Lastly the front-end can send requests to the MySQL instance to INSERT the new entry.
### Development

#### Front End:
When the user goes to port 80 on the NGINX's IP, the information will be displayed as shown below, this section was added as my system would some times not work entirely so in order to provide evidence of it working this image has been added:
![image](https://user-images.githubusercontent.com/86304577/129507822-4be08bb9-cf51-4713-a107-924839ded5ee.png)

##### Unit Testing:
Unit testing is used to test each services app.py and see whether they function. Once this script is completed Jenkins will display a report that shows if the testing was successful and provides a report that shows the percentage of the application tested.
![image](https://user-images.githubusercontent.com/86304577/129508662-3ee7bf3a-e3f1-4732-8f33-da47962aaf0c.png)
![image](https://user-images.githubusercontent.com/86304577/129508379-9bb27e5f-b94e-41fe-96bb-ed65f50dc9b1.png)

### Footer
#### Future Improvements
1. To decrease total time of build, push and deploy.
2. Implement Integration testing using Selenium although it is not needed it will be a big help for bigger projects with larger databases and functionalities.
3. Given more time have a more appealing front-end.

#### Author
Thushith Premadas

#### Acknowledgements
Oliver Nichols

#### Versions
15/08/2021 -v1.0.0
















