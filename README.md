# Birdbot
A python bot to execute commands on Linux or Kubernetes systems with the use of Discord as a medium.


I made this bot so that ultimately I could make it so users on Discord would not need to have access to the actual box that some game servers would run on so that they could fetch logs or restart the game server if needed.

Since then I have refined the bot and made it so that I can run kubectl commands with the addition of a Service Account on my Kubernetes Clusters.

You may use this bot either as a container image or with a simple python command. The bot is compatible with python 3.13.

Please note that it is expected that you will clone this repo and add/remove your own features as needed rather than use this as is. 

## Environmental Variables

| Envar | Purpose | Default |
| :----: | --- | --- |
| `PUID=1000` | To set the UserID for the bot user | `1000` |
| `PGID=1000` | To set the GroupID for the bot user | `1000` |
| `HOSTNAME=birdbot` | Set the hostname of the container for easier identification when invoking !test. | `birdbot` |
| `TOKEN=token` | This is required to run the bot. If you don't set this the bot will continuously crash. | `token` THIS WILL FAIL IF LEFT DEFAULT |
| `PREFIX=!` | The prefix you would like to use to execute commands eg. !test or -test | `!` |

## Using with Kubernetes
This is the intended use of the bot. Before doing this you will need to build the image using docker and to push the image to a registry of your choosing as Kubernetes does not use Local images and only images from a registry.
For this example we will be using DockerHub since it's the most common.
1. First clone the repo. ```git clone https://github.com/unixbird/birdbot.git```
2. ```cd birdbot```
3. ```docker build -t dockerusername/examplename .```
4. ```docker push dockerusername/examplename```
   After you push this to a registry you will need to setup a Service Account for your deployment/pod. 
   
5. ```kubectl create ns examplename``` <<< This is optional if you don't intend to have the resources in a different namespace other than default.
6. From the examples folder, we will use the serviceaccount.yml file. After you edit it to your needs run:
   ```kubectl apply -f examples/serviceaccount.yml -n examplenamespace```
7. After this step you may go ahead and run: ```kubectl apply -f examples/deployment.yml -n examplenamespace```
   
   The bot should be up. You can check with the ```kubectl -n examplename logs -l app=birdbot``` to see the (Bot Ready) message. If the bot is crashing make sure you have the correct Secret token inserted into the ENVAR. 
   If you don't receive an error go ahead and head over to the [Discord Developer portal](https://discord.com/developers/applications) and create a bot link to invite the bot to your discord. 

## Using this with python
By far the simplest method but not it's intended use. All that you would need to do is insert your Bot Token into the ('TOKEN') field after you have edited the python script to your liking and run:

``` python birdbot.py ```

After this the bot will be running and you will need to invite it to the Guild (Discord Server) by creating an invite link from the [Discord Developer portal](https://discord.com/developers/applications) 

The default command to test is ```!test``` in the discord channel.

-------------------------------------------------------------


