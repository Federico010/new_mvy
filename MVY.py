import sys, time
import subprocess
from time import sleep
import telepot
from telepot.loop import MessageLoop
import os
import youtube_dl
from apiclient.discovery import build

#service = build("customsearch", developerKey="AIzaSyDd3MMLX8tseaNGQPpcKUEc2wTb1ST_t2w")
x = 0
a = 0

settingformat = []
alluser = []
settinglanguage = []
languageing = []

def rispondi(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    language = msg['from']['language_code']
    print(msg)
    print(command)
    print(language)
    if chat_id != 713333320:
        bot.sendMessage(713333320, command)
        bot.sendMessage(713333320, msg)
    if language == 'it':
        if chat_id in languageing:
            print('None')
        else:
            settinglanguage.append(chat_id)
        
    v = 0
    vtot = 0
    
    def startita():
    	bot.sendMessage(chat_id, 'Benvenuto.\nQuesto bot è in grado di scaricare musica da Spotify e i video delle canzoni.\nCambia le impostazioni prima di iniziare.\n/settings\nScrivi il nome della canzone per scaricarla e scegli se scarucare il video')
    	bot.sendMessage(chat_id, 'Per qualsiasi problema, o traduzione sbagliata contatta @WWWDownloaderAdmin')
    	bot.sendMessage(chat_id, 'Per sostenere il bot donaci, ne saremo grati.\n/donate')
    def starting():
    	bot.sendMessage(chat_id,'Welcome.\nThis bot is able to download videos and audios from youtube and many other sites.\nChange your settings before you begin.\n/settings\n/list to see the sites that support downloading.\nWrite Yt and the name of the song to download it (Yt Hollywood\'s Bleeding).\n/d link to download the video from youtube (/d https://www...).\n/a link to download an audio (/a https://www...).')
    	bot.sendMessage(chat_id, 'For any problem, or wrong translation, contact @WWWDownloaderAdmin')
    	bot.sendMessage(chat_id, 'To support the bot donate us, we will be grateful.\n/donate')
    
    if command == '/start':
        if chat_id in settinglanguage:
            startita()
        else:
            starting()
        alluser.append(chat_id)
    elif command == '/donate':
        bot.sendMessage(chat_id,'paypal.me/MVYdownloader')
    elif '/avviso' in command:
        avviso = command.replace("/avviso ", "")
        for i in alluser:
        	vtot=vtot+1
        while True:
            try:
                for i in alluser:
                    bot.sendMessage(alluser(v), avviso)
                    if i == vtot:
                       break
            except:
                bot.sendMessage(713333320, v)
                alluser.remove(str(alluser(i)))
    elif '/alluser' in command:
        imp = command.replace("/alluser alluser: ","")
        imp1 = imp.replace("[","'")
        imp2 = imp1.replace("]","'")
        imp3 = imp2.replace(",","',")
        imp4 = imp3.replace(" "," '")
        print(imp4)
        alluser.append(imp4)
    elif '/settinglanguage' in command:
        imp = command.replace("/settinglanguage settinglanguage: ","")
        imp1 = imp.replace("[","'")
        imp2 = imp1.replace("]","'")
        imp3 = imp2.replace(",","',")
        imp4 = imp3.replace(" "," '")
        print(imp4)
        settinglanguage.append(imp4)
    elif command == '/Eng':
        languageing.append(chat_id)
        settinglanguage.remove(chat_id)
        bot.sendMessage(chat_id, 'Selected language.')
        starting()
    elif command == '/Ita':
        settinglanguage.append(chat_id)
        languageing.remove(chat_id)
        bot.sendMessage(chat_id, 'Lingua selezionata')
        startita()
    elif command == '/settings':
        if chat_id in settinglanguage:
            bot.sendMessage(chat_id, 'Cambia lingua\n/Ita\n\n/Eng')
            bot.sendMessage(chat_id, 'Scegli il formato del download con il comando Yt. Clicca su di esso per selezionarlo\n/flac\nMiglior qualità audio, ma ha occupa più spazio\n\n/mp3\nQualità audio inferiore ma occupa molto meno spazio')
        else:
            bot.sendMessage(chat_id, 'Change language\n/Ita\n\n/Eng')
            bot.sendMessage(chat_id, 'Choose the Yt command download format. Click on it to select it\n/flac\nBetter audio quality but takes up wider\n\n/mp3\nLower audio quality but less wide')
    elif command.startswith('http'):
        if chat_id in settinglanguage:
            bot.sendMessage(chat_id, 'Comando errato. Se volevi scaricare un video scrivi il link dopo (/d), invece se volevi scaricare un audio scivilo dopo (/a)')
        else:
            bot.sendMessage(chat_id, 'Incorrect command. Please if you want to download a video write (/d) before the Link, instead if you want to download an audio write (/a)')
    elif command == '/export':
        bot.sendMessage(713333320, 'alluser:\n'+str(alluser))
        bot.sendMessage(713333320, 'settinglanguage:\n'+str(settinglanguage))
    elif '/d' in command:
        videod = command.replace("/d ", "")
#        named = videod.replace("https://", "")
        y = x
        bot.sendMessage(chat_id, '.....')
        options = {
            'outtmpl': str(y) + '.mp4',
	        'format': 'bestvideo/best',
        }

        x + 1
        print(x)
        filename = str(y) + '.mp4'
        print(filename)
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([videod])
            b = os.path.getsize(filename)
            print(b)
            if b > 51380224:
                if chat_id in settinglanguage:
                    bot.sendMessage(chat_id, 'Il file è troppo grande, per non bloccare il bot manda il messaggio che hai appena inviato a @MVY_official_bot\nIl file verrà inviato appena disponibile.')
                else:
                    bot.sendMessage(chat_id, 'The file is too large, to not block the bot, send the message you just sent to @MVY_official_bot\nThe file will be sent as soon as available.')
            else:
                bot.sendVideo(chat_id, video=open(filename, 'rb'))
                print("Sent!")
            os.remove(filename)
    elif '/a' in command:
        audiod = command.replace("/a ", "")
        namea = audiod.replace("https://", "")
        b = a
        bot.sendMessage(chat_id, '.....')
        options = {
            'outtmpl': namea + str(b) + '.mp3',
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
            }]
        }
        a + 1
        print(a)
        filename = namea + str(b) + '.mp3'
        print(filename)
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([audiod])
            b = os.path.getsize(filename)
            print(b)
            if b > 51380224:
                if chat_id in settinglanguage:
                    bot.sendMessage(chat_id, 'Il file è troppo grande, per non bloccare il bot manda il messaggio che hai appena inviato a @MVY_official_bot\nIl file verrà inviato appena disponibile.')
                else:
                    bot.sendMessage(chat_id, 'The file is too large, to not block the bot, send the message you just sent to @MVY_official_bot\nThe file will be sent as soon as available.')
            else:
                filename = open(filename, 'rb')
                bot.sendAudio(chat_id, filename)
                filename.close()
                print("Sent!")
            os.remove(filename)

    elif command.startswith('Yt'):
        comando = command.replace("Yt ", "")
        res = service.cse().list(
            q=comando,
            cx='009017419182529177498:s6vbjjafkux',
            num=1,
        ).execute()
        if not 'items' in res:
            if chat_id in settinglanguage:
                bot.sendMessage(chat_id, 'Nessun risultato!\nRipova.')
            else:
                bot.sendMessage(chat_id, 'No result!\nTry again')
        else:
            for item in res['items']:
                bot.sendMessage(chat_id, item['title'])
                bot.sendMessage(chat_id, item['link'])
                video = str(item['link'])
                titolo = str(item['title'])
                print(video)
#                titolo = titolo.replace(" - YouTube", "")
                print(titolo)
                bot.sendMessage(chat_id, '.....')
                options = {
                    'format': 'bestaudio/best',
                    'outtmpl': titolo + '.mp3',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '320'
                    }]
                }
            watchid = video.replace("https://www.youtube.com/watch?v=", "")
#           filename = titolo+"-"+watchid+".mp3"
            filename = titolo + ".mp3"
            outputflac = titolo + ".flac"
            print(filename)
            with youtube_dl.YoutubeDL(options) as ydl:
                ydl.download([video])
                b = os.path.getsize(filename)
                print(b)
                if b > 51380224:
                    if chat_id in settinglanguage:
                        bot.sendMessage(chat_id, 'Il file è troppo grande, per non bloccare il bot manda il messaggio che hai appena inviato a @MVY_official_bot\nIl file verrà inviato appena disponibile.')
                    else:
                        bot.sendMessage(chat_id, 'The file is too large, to not block the bot, send the message you just sent to @MVY_official_bot\nThe file will be sent as soon as available.')
                else:
                    filename = open(filename, 'rb')
                    bot.sendAudio(chat_id, filename)
                    filename.close()
                    print("Sent!")
                os.remove(filename)


bot = telepot.Bot('1796502065:AAG1s3kRoYNYd1_oR4FcDmmZgJq_8az_5Ro')
print('[+] Server is Listenining [+]')
print('[=] Type Command from Telegram [=]')

if __name__ == "__main__":
    bot.message_loop(rispondi)
    while True:
        sleep(3)