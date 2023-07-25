from linkConvert import ytdl
import this

import dipInfo


import discord
from discord.ext import commands
# import speedtest
from muradian import msc
import wikipedia

# intention area
discord.Intents.default().message_content = True

client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    print("message content loaded")


@bot.event
async def on_ready():
    print(f'logged in as {client.user}')
    try:
        synced = await client.tree.sync()
        print("Bot commands Loaded")

    except Exception as e:
        print(e)


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
            await message.channel.send(
                "Murad is my Developer/ Creator 🥰 . His skill on  discord server is awesome 🥰 you can hire him ")

    # normal message area

    elif 'hello' == message.content.lower():
        await message.channel.send("Hello ! আপনি কেমন আছেন ?")

    elif 'bye' == message.content[0:].lower():

        await message.channel.send("Take care ! ")

    elif 'fuck' in message.content.lower() or 'bokachoda' in message.content.lower():
        await message.channel.send('খারাপ ভাষা ব্যবহার করা কি ভাল?')

    elif 'murad' == message.content.lower():
        await message.channel.send('মুরাদ এখন ব্যস্ত, আমার সাথে শেয়ার করতে পারেন !')

    elif 'who is sushanto' in message.content.lower() or 'who is sushanto roy' in message.content.lower():
        await message.channel.send('সুশান্ত কুমার রায় ! তিনি **Dream it Possible ** গ্রুপের অন্যতম সেরা সদস্য, '
                                   'তিনি খুব ভদ্র ছেলে এবং তিনি সবসময় সম্পর্ক আরও ভাল করার চেষ্টা করেন।')

    elif 'who is junayed' in message.content.lower() in message.content.lower() or 'who is junayed ahmed' in message.content.lower():
        await message.channel.send('জুনায়েদ আহমেদ! তিনি তার ফিটনেস এবং ক্রিকেটপ্রেমী হিসেবে বিখ্যাত। তিনি **Dream it '
                                   'Possible** গ্রুপের সদস্য ')

    elif 'who is ajoy' in message.content.lower() in message.content.lower() or 'who is ajoy saha' in message.content.lower():
        await message.channel.send('অজয় সাহা, তিনি সংগ্রাম এবং প্রেরণার জন্য বিখ্যাত। তিনি ডিপের একজন গুরুত্বপূর্ণ '
                                   'সদস্য এবং বর্তমানে তিনি **Dream it possible** গ্রুপের মডারেটর হিসাবে কাজ করছেন।')

    elif 'who is hasnat' == message.content.lower() or 'who is hasnat hridoy' == message.content.lower():
        await message.channel.send('হাসনাত হৃদয়! তিনি তার অত্যধিক চিন্তার জন্য বিখ্যাত শুধু তাই নয়, তার একটি ভাল '
                                   'লক্ষণও রয়েছে যে তিনি গুরুতরভাবে তার নিজের বাহক হিসাবে গড়ে উঠেছে। তিনি **Dream '
                                   'it possible** গ্রুপের শিক্ষক ও পরামর্শদাতা হিসাবে কাজ করছেন।')

    elif 'who is murad' == message.content.lower() or 'who is m a murad' == message.content.lower():
        await message.channel.send('এম এ মুরাদ! তিনি **Dream it Possible** গ্রুপের প্রতিষ্ঠাতা এবং সিইও। সেও আমাকে '
                                   'ডেভেলপ করছে,দিন দিন আমি আরও এগিয়ে যাচ্ছি উন্নয়নশীল ভবিষ্যতের দিকে')

    else:
        print("print running")

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
