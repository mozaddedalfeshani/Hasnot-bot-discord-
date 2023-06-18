import this

import discord
import speedtest
from muradian import msc
import wikipedia

TOKEN = 'MTA2Nzk0OTk4MDM4NTU0NjMzMA.Ggy8Xu.C_GhYYHeb3OEm01E6GvHPnFml2BykwkgMGeiWE'

from linkConvert import ytdl

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    give = message.content



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

        elif (command_key == 'src'):
            await message.channel.send('I am trying to answering your question! ')
            com = message.content[7:]
            # print(com)
            try:
                sms = wikipedia.summary(com, sentences=1)
                await message.channel.send(sms)

            except:
                await message.channel.send('I am sorry , I can\'t answer this ! ')
                await message.channel.send("You can report us whcih quedtion I fialed")
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
            await message.channel.send("Murad is my Developer/ Creator 🥰 . His skill on  discord server is awesome 🥰 you can hire him ")

        elif message.content.lower() == 'bye':
            await message.channel.send("Take care ! ")



    # else:
    #     print('start')
    #     @client.event()
    #     async def on_message_edit(before, after):
    #         await before.channel.send(
    #             f'{before.author} edit a message.\n'
    #             f'Before: {before.content}\n'
    #             f'After: {after.content}\n'
    #         )


client.run(TOKEN)
