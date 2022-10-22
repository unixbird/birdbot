import os
import sys
import discord
import subprocess

# discord client
client = discord.Client()


def process_message(message):
    args = message.content.split(" ")

    return args

# create a new event that lets us know the bot is up
@client.event
async def on_ready():
     print("Its birbin time!")
     print("(Bot Ready)")

# listen for specific messages
@client.event
async def on_message(message):
# igore the following lines as they were experimental
#    client.on('message', msg => {
#    if (msg.channel instanceof Discord.DMChannel
#        const Reject = new Discord.MessageEmbed()
#            .setColor("#FF0000")
#            .setTitle('Error')
#            .setDescription('This command can only be used in the server.')
#        msg.author.send(Reject);
#   A simple message to test to make sure the bot is listening and can respond to discord messages
    if message.content.startswith("!test"):
        hostname = os.environ.get('HOSTNAME')
        await message.channel.send(hostname+ ' is alive')
#   Examples of being able to have the bot run kubectl rollout commands for deployments upon message
    if message.content.startswith("!zomboid-restart"):
        args = process_message(message)
        result = subprocess.call(["kubectl", 'rollout', 'restart', 'deployment/zomboid-deployment'])
        if result == 0:
          await message.channel.send("executed restart of Zomboid")
    if message.content.startswith("!librespeed-rollout"):
        args = process_message(message)
        result = subprocess.call(["kubectl", 'rollout', 'restart', 'deployment/librespeed-deployment'])
        if result == 0:
          await message.channel.send("Redployed librespeed")
#   example command for the bot to execute a script on the host if used outside of a container or if the script exists on the container
    if message.content.startswith("/brio-start"):
        args = process_message(message)
        result = subprocess.call(["sh", '/home/birdbot/botscripts/briostart.sh'])
        await message.channel.send("Started Briomarea service")
#   example command to print the contents a log file to the discord channel 
    if message.content.startswith("/brio-quicklogs"):
        args = process_message(message)
        result = file = open(r"/home/steam/brio/server.log", "rt")
        content = file.read()
        await message.channel.send(content)
#   example command to SEND the log file itself to the discord channel
    if message.content.startswith("/brio-logs"):
        await message.channel.send(file=discord.File('/home/steam/brio/server.log'))

# Required to run the bot
bot = os.environ.get('TOKEN')
client.run(bot)
