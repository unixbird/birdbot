import os
import sys
import discord
import subprocess
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

prefix = os.environ.get('PREFIX')
bot = commands.Bot(command_prefix=(prefix), intents=intents)

#this simply just echos the current server where this command was executed
@bot.command()
@commands.has_role("YOURDISCORDROLE")
async def hello(ctx):
    await ctx.send(ctx.guild)

#simple command to see where the host is and if its up
@bot.command()
async def test(ctx):
    hostname = os.environ.get('HOSTNAME')
    await ctx.send(hostname+ ' is alive')

# example command on how to restrict to a specific role in discord in a specific server and executing a simple kubectl rollout restart command
@bot.command()
@commands.has_role("YOURDISCORDROLE")
async def zomboidrestart(ctx):
    discordserverid = YOURDISCORDSERVERID
    server = ctx.message.guild
    if server.id == discordserverid:
      result = subprocess.call(["kubectl", 'rollout', 'restart', 'deployment/zomboid-deployment'])
      await ctx.send("executed restart of Zomboid")

# example if you didn't want to bind a specific role to a command
@bot.command()
async def sptclientrestart(ctx):
    server = ctx.message.guild
    result = subprocess.call(["kubectl", 'rollout', 'restart', 'deployment/sptclient-deployment'])
    await ctx.send("executed restart of the SPT Client")

    
# ------------------------------
# beyond this point is code before the change to bot.commands and is to only be used as reference! It is HIGHLY recommended to use bot.command instead
async def on_message(message):
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
token = os.environ.get('TOKEN')
bot.run(token)                          
