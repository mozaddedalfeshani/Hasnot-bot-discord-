# import area
import discord
import discord.ext
import wikipedia
# from to import
from muradian import msc
import datetime
from datetime import datetime

import components.dipFun
from discord.ext import commands
import components.dipInfo as di
from components.dipFun import dipRandom as dipRan
from components.lineConvert import hh_ctd
from components.linkConvert import ytdl
from components.resultPage import resultPage as gr


#firebase section

import firebase_admin
from firebase_admin import firestore

from firebase_admin import credentials

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
# data ={
#     "name": "murad"
# }
# db.collection('Hello').add(data)
# intention area
discord.Intents.default().message_content = True
discord.Intents.voice_states = True #enable the voice states true
client = discord.Client(intents=discord.Intents.all())



@client.event
async def on_ready():

    print("message content loaded")
    print(f'Login time {datetime.now()}')


@client.event

async def on_voice_state_update(member, before, after):
    try:
        if before.channel != after.channel:  # Check for channel change
            if after.channel:
                # Retrive the guild name
                server_name = member.guild.name
                
                db.collection(str(server_name)).document('voice').collection(str(member.name)).add({
                    "voice":{
                        "name":member.name,
                        "Join": datetime.now()
                    }
                })

                print(before.channel.guild.name)
                print(f"{member.name} joined {after.channel.name}")
            else:
                server_name = member.guild.name
                db.collection(str(server_name)).document(str(member.name)).set({
                    "voice":{
                        "Leave": datetime.now()
                    }
                },merge=True)
                print(f"{member.name} left {before.channel.name}")
    except Exception as err:
        print(err)

@client.event
async def on_message(message):

    try:
        database = {
            message.channel.name :{
                "Messgae": message.content,
                str(datetime.now()):{
                    "Message": message.content,
                    "Time": datetime.now()
                }
                
            }
        }
        db.collection(message.guild.name).document(str(message.author.name)).set(database,merge=True)
    except Exception as err:
        print(err)

    print(f"{message.author.name} (ID: {message.author.id}) sent message in '{message.channel.name}':")

    if message.author == client.user:
        print(f'{message.author} and => {client.user}')
        print(f"{message.author.name} (ID: {message.author.id}) sent message in '{message.channel.name}':")
        print(message.content)
        return

    give = message.content
    # print(give)

    if message.content.startswith('hh'):
        if message.content.lower() == 'hh help':
            await message.channel.send("https://imurad12.blogspot.com/2023/08/not-discord-bot-documentation.html")
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
                await message.channel.send('> I am really sorry! I can\'t understand ! ')
                await message.channel.send(
                    '> Please folow this system: hh clc \{digit_count\} \{first Digit\} \{operator\} \{last digit\} ')

        # serching function
        elif (command_key == 'src'):
            await message.channel.send('I am trying to answering your question! ', delete_after=2)
            com = message.content[7:]

            # print(com)
            try:
                page = wikipedia.page(com)
                sms = wikipedia.summary(com, sentences=1)
                await message.channel.send(sms)
                await message.channel.send(page.url)

            except Exception as e:
                print(e)
                await message.channel.send('> I am sorry , I can\'t answer this ! ', delete_after=5)
                await message.channel.send("> You can report to us \n> Link : https://discord.gg/VZ93PYTS5e")

        elif (command_key == 'fli'):
            com = message.content[8:]
            await message.channel.send(com[::-1])

        elif (command_key == 'ytd'):
            text = message.content[8:]
            lol = ytdl(text)
            await message.channel.send(">  Here the Download link: ")
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

        elif (command_key == 'who' and len(message.content) == 6):

            x = dipRan.who()
            await message.channel.send(f' {message.author.mention} \n > Selected person is **{x}** 💐')

        elif (command_key == 'mog'):

            name = message.content
            name = name[7:]
            x = name.split()
            last = len(x) - 1
            # print(f'last : {last}')
            y = int(x.pop(last))  # given last digit damn sure
            x.pop(last - 1)  # final list

            result = dipFun.dipRandom.givenWhoGroup(x, y)
            await message.channel.send(f' > The random are : \n > {result}')

        elif (command_key == 'ctd'):

            x = hh_ctd.create_thread_hh(message.content)
            thread = await message.channel.create_thread(
                name=x
            )
            await message.channel.send(f"{message.author.mention} Successfully create private Thread")
            await thread.send(f'{message.author.mention} create this Thread ')

        elif 'hhreact' in message.content:
            await message.add_reaction('👍')
            await message.add_reaction('👎')
            await message.add_reaction('❤️')
            await message.add_reaction('🤣')
            await message.add_reaction('😢')
            await message.add_reaction('😡')

    # normal message area
    elif 'hhreact' in message.content:
        await message.add_reaction('👍')
        await message.add_reaction('👎')
        await message.add_reaction('❤️')
        await message.add_reaction('🤣')
        await message.add_reaction('😢')
        await message.add_reaction('😡')

    elif message.content == "who is amily":
        await message.channel.send(" > Amily is shanto\'s GF! And our vabi")

    # Emojy get  section

    elif (
            'vote me' in message.content.lower() or 'vote kor' in message.content.lower() or 'vote de' == message.content.lower()):
        # print(message.content)
        emoji = '\N{THUMBS UP SIGN}'
        emoji_2 = '\N{THUMBS DOWN SIGN}'

        await message.add_reaction(emoji)
        await message.add_reaction(emoji_2)
        await message.add_reaction('🥶')

    elif 'hello' == message.content.lower():
        await message.channel.send(f"Hello {message.author.mention} ! আপনি কেমন আছেন ?")

    elif 'bye' == message.content[0:].lower():

        await message.channel.send(f"{message.author.mention} Take care ! ")

    elif 'fuck' in message.content.lower() or 'bokachoda' in message.content.lower():
        await message.channel.send(f' {message.author.mention} খারাপ ভাষা ব্যবহার করা কি ভাল?')

    elif 'murad' == message.content.lower() or 'hasnat' == message.content.lower() or 'shanto' == message.content.lower() or 'junayed' == message.content.lower() or 'juna' == message.content.lower() or 'aong' == message.content.lower() or 'ajoy' == message.content.lower() or 'sushanto' == message.content.lower():
        name = message.content
        await message.channel.send(f'{message.author.mention}\n > {di.busyList(name)}')

    elif 'who is sushanto' in message.content.lower() or 'who is sushanto roy' in message.content.lower():
        await message.channel.send(f'{message.author.mention}\n > {di.person("shanto")}')

    elif 'who is junayed' in message.content.lower() in message.content.lower() or 'who is junayed ahmed' in message.content.lower():
        await message.channel.send(f'{message.author.mention}\n > {di.person("junayed")}')

    elif 'who is ajoy' in message.content.lower() in message.content.lower() or 'who is ajoy saha' in message.content.lower():
        await message.channel.send(f'{message.author.mention}\n > {di.person("ajoy")}')

    elif 'who is hasnat' == message.content.lower() or 'who is hasnat hridoy' == message.content.lower():
        await message.channel.send(f'{message.author.mention}\n > {di.person("hasnat")}')

    elif 'who is murad' == message.content.lower() or 'who is m a murad' == message.content.lower():
        x = di.person("murad")

        await message.channel.send(f'{message.author.mention} \n > {x}')

        # thread = await message.channel.create_thread(
        #     name="example"
        # )
        # print(message.channel)
        # await thread.send("This is an example message")

    else:
        @client.event
        async def on_message_edit(before, after):
            x = before.content
            print(client.user.id)
            if (message.author.id != 1067949980385546330):
                await before.channel.send(

                    f' **{before.author.mention}** edit a message.\n'
                    f'> Before:  {di.strike(x)} \n'
                    f'> After: {after.content}\n', delete_after=5
                )


client.run(
    TOKEN)
