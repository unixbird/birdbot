import os
import sys
import discord
import subprocess
from discord.ext import commands
    
prefix = os.environ.get('PREFIX')
bot = commands.Bot(command_prefix=(prefix))

@bot.command()
@commands.has_role("AEG Swagmin")
async def hello(ctx):
    await ctx.send(ctx.guild)

@bot.command()
async def test(ctx):
    hostname = os.environ.get('HOSTNAME')
    await ctx.send(hostname+ ' is alive')

@bot.command()
@commands.has_role("AEG Swagmin")
async def zomboidrestart(ctx):
    result = subprocess.call(["kubectl", 'rollout', 'restart', 'deployment/zomboid-deployment'])
    if result == 0:
      await ctx.send("executed restart of Zomboid")

@bot.command()
@commands.has_role("SysOps")
async def librespeedrestart(ctx):
    result = subprocess.call(["kubectl", 'rollout', 'restart', 'deployment/librespeed-deployment'])
    if result == 0:
      await ctx.send("redeployed Librespeed")

# ------------------------------
# beyond this point is code before the change to bot.commands and is to only be used as reference! It is HIGHLY recommended to use bot.commands instead
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
