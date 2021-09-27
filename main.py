import discord
import time
TOKEN = '' #tokenhere
client = discord.Client()
@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
@client.event
async def on_message(message):

    if message.content.startswith('$pomodoro'):
        msg=message.content.split()
        if(len(msg)<2):
            await message.channel.send('You need to specify the time like, for example $pomodoro 20')
        else:
            pomodoro_time=int(msg[1])
            pomodoro_time_init=pomodoro_time
            await message.channel.send('Working for '+str(pomodoro_time) +' minutes')
            while(pomodoro_time>0):
                time.sleep(60)
                pomodoro_time=pomodoro_time-1
                if(pomodoro_time!=0):
                    await message.channel.send("You have to study: "+str(pomodoro_time_init)+" minutes\nRemaning : "+str(pomodoro_time)+"minutes")
            await message.channel.send('You are done!! Congratulations. You worked hard for '+str(pomodoro_time_init) +' minutes, now take a break.')
    if message.content.startswith('$hello'):
        await message.channel.send('Hello')

client.run(TOKEN)
