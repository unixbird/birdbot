# Birdbot
A python bot to execute commands on Linux or Kubernetes systems with the use of Discord as a medium.


I made this bot so that ultimately I could make it so users on Discord would not need to have access to the actual box that some game servers would run on so that they could fetch logs or restart the game server if needed.

Since then I have refined the bot and made it so that I can run kubectl commands with the addition of a Service Account on my Kubernetes Clusters.

Currently this bot comes with the Discord module and the Kubectl binary.

You may use this bot either as a container image or with a simple python command. The bot is compatible with python 3.8.

## Using with Kubernetes
This is the intended use of the bot. Before doing this you will need to build the image using docker and to push the image to a registry of your choosing as Kubernetes does not use Local images and only images from a registry.
For this example we will be using DockerHub since it's the most common.

1. ```docker build . -t yourusernameondockerhub/examplename --no-cache```
   (The ```--no-cache``` is used because whenever I build the image it may already have the adding of the python script cached. This is to insure that      we get the newest script that was modified.)
2. ```docker push yourusernameondockerhub/examplename```
   After you push this to a registry you will need to setup a Service Account for your deployment/pod. 
   
1. ```kubectl create ns examplename```
2. From the examples folder, we will use the serviceaccount.yml file. After you edit it to your needs run:
   ```kubectl apply -f serviceaccount.yml```
3. After this step you may go ahead and run: ```kubectl apply -f deployment.yml -n examplename```
   
   The bot should be up. You can check with the ```kubectl -n examplename logs -l app=birdbot``` to see the (Bot Ready) message. If the bot is crashing make sure you have the correct Secret token inserted into the ENVAR. 
   If you don't receive an error go ahead and head over to the [Discord Developer portal](https://discord.com/developers/applications) and create a bot link to invite the bot to your discord. 
   Depending on what the bot does I highly recommend that you keep the bot segregated into its own channel with only trusted users. 

## Using this with python
By far the simplest method all that you would need to do is insert your Bot Token into the ('TOKEN') field after you have edited the python script to your liking and run:

``` python birdbot.py ```

After this the bot will be running and you will need to invite it to the Guild (Discord Server) by creating an invite link from the [Discord Developer portal](https://discord.com/developers/applications) 

The default command to test is ```!test``` in the discord channel.

-------------------------------------------------------------


