def ytdl(text):
    # https://www.youtube.com/watch?v=o1ARBxpp4Ss
    link = text[:19] + "pp" + text[19:]
    return link

def answer(text):
    if(text=="how are you"):
        return 'Fine! Thank\'s for asking me '

    if(text== 'who are you'):
        reply = f'Mainly I am bot for daily services :) '
        return reply