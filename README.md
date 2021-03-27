# A Devops Task

### Description 
Docker framework with Python script to convert json to xml, encrypt and transfer between containers

### Technical Requirements
Python,Docker


### How to
- Drop the json file(s) in src folder
- Start the containers using below command
```
$ docker-compose up
```
- Verify the xml file(s) with both encrypted and decrypted in dest folder

# How using GitHub Action.
- add DockerHub Credentials to Secret.
- create workflows.
- create an Image and upload to dockerHub.
- create Default UbuntuVM and run containers inside VM using ```docker-compose up```.
- create steps to verify content.
- close the workflow.


