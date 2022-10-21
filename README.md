# Birdbot
A python bot to execute commands on Linux or Kubernetes systems


I made this bot so that ultimately I could make it so users on Discord would not need to have access to the actual box that some game servers would run on so that they could fetch logs or restart the game server if needed.

Since then I have refined the bot and made it so that I can run kubectl commands with the addition of a Service Account on my Kubernetes Clusters.

Currently this bot comes with the Discord module and the Kubectl binary.

You may use this bot either as a container image or with a simple python command. The bot is compatible with python 3.8.

## Using without Docker/Kubernetes
By far the simplest method all that you would need to do is insert your Bot Token into the ('TOKEN') field after you have edited the python script to your liking and run:

``` python birdbot.py ```

After this the bot will be running and you will need to invite it to the Guild (Discord Server) by creating an invite link from the [Discord Developer portal](https://discord.com/developers/applications) 

The default command to test is ```!test``` in the discord channel.

-------------------------------------------------------------

## Using with Kubernetes
This is the intended use of the bot.
