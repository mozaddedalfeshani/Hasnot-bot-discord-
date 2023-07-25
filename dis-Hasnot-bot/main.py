import wikipedia
from muradian import msc
from discord.ext import commands
import discord
import speedtest
from linkConvert import ytdl
import time
import resultPage

from resultPage import resultPage as gr


import dipInfo as di
# import dipInfo
# from dipInfo import dipInformation
# from dipInformation import person

TOKEN = "MTA2Nzk0OTk4MDM4NTU0NjMzMA.G_MscM.4ZWOTXtxyFuNA5P5VKrESw-Uw40z0_WZUnZULY"
# import speedtest

# intention area
discord.Intents.default().message_content = True

client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    print("message content loaded")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    give = message.content
    print(give)

    if (message.content.startswith('hh')):
        command_key = message.content[3:6]
        # summation
        if command_key == 'sum':
            text = message.content[7:]
            ans = msc.msum(text)
            await message.channel.send(ans)
        # string line for calculation
        elif (command_key == 'clc'):
            text = message.content[7:]
            # print(text)
            try:
                await message.channel.send(msc.stca(text))

            except:
                await message.channel.send('I am really sorry! I can\'t understand ! ')
                await message.channel.send('Please folow this system: hh clc digit_count \{digit\'s by space\}')

        # serching function
        elif (command_key == 'src'):
            await message.channel.send('I am trying to answering your question! ')
            com = message.content[7:]
            # print(com)
            try:
                sms = wikipedia.summary(com, sentences=1)
                await message.channel.send(sms)

            except:
                await message.channel.send('I am sorry , I can\'t answer this ! ')
                await message.channel.send("You can report us on my Admin server")
                await message.content.send("Link : https://discord.gg/VZ93PYTS5e")

        elif (command_key == 'fli'):
            com = message.content[8:]
            await message.channel.send(com[::-1])

        elif (command_key == 'ytd'):
            text = message.content[8:]
            lol = ytdl(text)
            await message.channel.send(" Here the Download link: ")
            # sending the link from here
            await message.channel.send(lol)

        elif (command_key == 'avg'):
            text = message.content[7:]
            await message.channel.send(msc.mavg(text))

        elif (command_key == 'srr'):
            # hh result 221156047
            id = message.content[7:16]
            if len(id) == 9:

                try:
                    value = gr.getResult(id)

                except:
                    print("Fail to load")
                    pass

                await message.channel.send(f'{value} ')

            else:
                await message.channel.send("Enter the valid Id for get result")

        elif (command_key == 'ser'):
            if (message.content == 'hh server speed'):
                await message.channel.send("please wait few second :)")

                test = speedtest.Speedtest()
                down = test.download()
                up = test.upload()
                ans = f'Internet Speed of server is:\nDownload: {down / 1024 / 1024 / 8 :.3f} Mbps \nUpload: {up / 1024 / 1024 / 8 :.3f} Mbps'

                await message.channel.send(ans)

            # it's on working ! Very soon this feature will come
        elif (message.content == "who is amily"):
            await message.channel.send("Amily is shanto\'s GF! And our vabi")

        elif message.content[:].lower() == "who is murad":
            await message.channel.send(

                "Murad is my Developer/ Creator 🥰 . His skill on  discord server is awesome 🥰 you can hire him ")

    # normal message area

    elif 'hello' == message.content.lower():
        await message.channel.send("Hello ! আপনি কেমন আছেন ?")

    elif 'bye' == message.content[0:].lower():

        await message.channel.send("Take care ! ")

    elif 'fuck' in message.content.lower() or 'bokachoda' in message.content.lower():
        await message.channel.send('খারাপ ভাষা ব্যবহার করা কি ভাল?')

    elif 'murad' == message.content.lower() or 'hasnat' == message.content.lower() or 'shanto' == message.content.lower() or 'junayed' == message.content.lower() or 'juna' == message.content.lower() or 'aong' == message.content.lower() or 'ajoy' == message.content.lower() or 'sushanto' == message.content.lower():
        name = message.content
        await message.channel.send(di.busyList(name))

    elif 'who is sushanto' in message.content.lower() or 'who is sushanto roy' in message.content.lower():
        await message.channel.send(di.person("shanto"))

    elif 'who is junayed' in message.content.lower() in message.content.lower() or 'who is junayed ahmed' in message.content.lower():
        await message.channel.send(di.person("junayed"))

    elif 'who is ajoy' in message.content.lower() in message.content.lower() or 'who is ajoy saha' in message.content.lower():
        await message.channel.send(di.person("ajoy"))

    elif 'who is hasnat' == message.content.lower() or 'who is hasnat hridoy' == message.content.lower():
        await message.channel.send(di.person("hasnat"))

    elif 'who is murad' == message.content.lower() or 'who is m a murad' == message.content.lower():
        x = di.person("murad")

        await message.channel.send(x)

    else:
        @client.event
        async def on_message_edit(before, after):
            x = before.content
            await before.channel.send(

                f' **{before.author}** edit a message.\n'
                f'Before:  {di.strike(x)} \n'
                f'After: {after.content}\n'
            )


client.run(TOKEN)
