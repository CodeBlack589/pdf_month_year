import datetime

from telethon.sync import TelegramClient,events
import configparser
config = configparser.ConfigParser()
config.read("copy.ini")

# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']

api_hash = str(api_hash)

phone = config['Telegram']['phone']
username = config['Telegram']['username']

with TelegramClient(username,api_id,api_hash) as client:
    messages=client.get_messages('https://t.me/UPSC_Prelims_Mains_PDF_Materials',limit=1000)

    year=int(input("Enter year for which you want do download the current affair file : "))
    print("1 for Jan,2 for Feb and so on if you type wrong then error show")
    month=int(input("Enter month for which you want do download the current affair file : "))
    if 1<=month<=12:
        x = datetime.datetime(year, month,1)
        y=x.strftime("%B")
        i=0
        data={}
        name={}
        for msg in messages:
            try:
                pdf_name=msg.media.document.attributes[0].file_name

                if "current" in pdf_name.lower() or "affairs" in pdf_name.lower() or "affairs" in pdf_name.lower():
                    d=msg.date.date()
                    k=str(d)
                    date=k.split("-")
                    if str(month) in str(date[1]) and str(year)==str(date[0]):
                        print(pdf_name)
                        i=i+1
                        name[i]=pdf_name
                        data[i]=msg
            except:
                continue
        if data:
            print("Total Number of files to be download : %s"%(len(data)))
            print("Your downloading started.........")
            k=0
            for x in data:
                k=k+1
                n=name[x]
                print("%s file download start...."%(k))
                client.download_media(data[x],"%s/%s/%s"%(year,y,n))

        else:
            print("No file at that time")

    else:
        print("wrong input")
