# Project

This is the document displaying all the steps required to create and deploy a simple python timestamp web application using docker.
1. After creating a simple python application that will display current data and time using flask, we need to dockerize it, to do that we need to follow sertain steps which are as follows.
2. First install docker, after that create a file named Dockerfile which will contain all the instructions required for the python application to run.
3. The dockerfile will contain commands which will install all the necessary dependancies required for the python application to work, after creating the dockerfile we need to build the docker image using "sudo docker build -t image-name ." command, after which a docker image will be created which will contain not only the python application but also all the necessary dependancies to main it work.
4. after the image is created we need to containerize it using "sudo docker run -itd --name container-name -p 5000:5000 image-name" command, after which a docker container will be created which will run the python application on the specified 5000 port on web. We can access the output of our python application there using the ip-address:5000.
5. I have deployed the python application using docker on my aws ec2 instance, so i could access it using my instance public ip address.
6. After creating the docker image and container, i have logged into my dockerhub repo using docker login command and uploaded the python application image into my repository using "docker push dockerhub-username/tag-name-of-the-image"
7. These were all the steps involved in creating and deploying a simple python application using docker.
