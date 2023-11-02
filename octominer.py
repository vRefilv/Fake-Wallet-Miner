from time import sleep as wait
import os
import ctypes
from forex_python.bitcoin import BtcConverter
from pick import pick
import string
import sys
import numpy
import keyboard
from os.path import exists
import urllib.request
from pystyle import Colors, Colorate, Write
import win32gui, win32con
from discord_webhook import DiscordWebhook, DiscordEmbed
hwnd = win32gui.GetForegroundWindow()
ctypes.windll.kernel32.SetConsoleTitleW("OctoMiner")
win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
theme = 0
bool1=False
def closen():
    ttk=4
    for i in range(0,3):
        ttk=ttk-1
        cls()
        print(Colors.red+'Closing in',end='\r')
        for i in range(0,4):
            print(Colors.red+'Closing in '+str(ttk),end='\r')
        wait(1)
    sys.exit('')
def cls():
    os.system('cls')

cls()
def cinput(texttoprint):
    global var
    var = Write.Input(texttoprint, Colors.blue_to_cyan, interval=0.0025)


cinput('enter license key: ')
license=var
if license == 'Octov1':
    cls()
    Write.Print("License Sucessfull\n\nWelcome User",Colors.blue_to_cyan, interval=0.0025)
    wait(1)
    dev_version = False
elif license == 'Octodev1':
        cls()
        Write.Print("License Sucessfull\n\nWelcome Dev",Colors.blue_to_cyan, interval=0.0025)
        wait(1)
        dev_version = True
else:
    cls()
    print(Colors.red + 'Bad License')
    wait(1)
    closen()


if dev_version==False:
    cls()
    print("Loading")

def internet_on():
    try:
        urllib.request.urlopen('http://google.com', timeout=1)
        return True
    except urllib.request.URLError as err:
        if dev_version == True: return True
        else: return False



def transfer():
    cinput('Enter your wallet:')
    ywallet=var
    if 'bc1' in ywallet or 'bc3' in ywallet and len(ywallet) >= 24 and len(ywallet) <= 31:
        cinput('Enter transfer wallet:')
        twallet=var
        if 'bc1' in twallet or 'bc3' in twallet and len(twallet) >= 24 and len(twallet) <= 31:
            print('Transfering from '+twallet+' to '+ywallet)
            wait(1)
            d=''
            for i in range(0,4):
                ctypes.windll.kernel32.SetConsoleTitleW('OctoMiner  ||  Transfering Wallets'+d)
                print(Colorate.Horizontal(Colors.blue_to_cyan, "[-] Transfering Wallets"+d, 1),end='\r')
                d=d+'.'
                wait(1)
            if  internet_on() == True:
                cls()
                ctypes.windll.kernel32.SetConsoleTitleW('OctoMiner  ||  '+'Transfer successful')
                print(Colors.green+'Transfer successful')
                wait(1)
                menui()
            elif internet_on() == False:
                ctypes.windll.kernel32.SetConsoleTitleW('OctoMiner  ||  '+'Unable transfer wallets')
                print(Colors.red+"[-] Unable to transfer Wallets")
                wait(2)
                print(Colors.red+'Check your internet connection')
                ctypes.windll.kernel32.SetConsoleTitleW('OctoMiner')
                wait(1)
                closen()

        else:
                cls()
                print(Colors.red+"Bad Wallets  |  Try again.")
                wait(1)
                cls()
                transfer()

    else:
            cls()
            print(Colors.red+"Bad Wallets  |  Try again.")
            wait(1)
            cls()
            transfer()



def miner(whatmining,lowlenght,maxlenght,randommin,randommax):
    loop = 0
    randbool = loop
    invalid = 0
    valid = 0
    money = 0
    cls()
    logo = """

                 ,.=ctE55ttt553tzs.,
             ,,c5;z==!!::::  .::7:==it3>.,
          ,xC;z!::::::    ::::::::::::!=c33x,
        ,czz!:::::  ::;;..===:..:::   ::::!ct3.
      ,C;/.:: :  ;=c!:::::::::::::::..      !tt3.
     /z/.:   :;z!:::::J  :E3.  E:::::::..     !ct3.
   ,E;F   ::;t::::::::J  :E3.  E::.     ::.     MttL
  ;E7.    :c::::F******   **.  *==c;..    ::     Jttk
 .EJ.    ;::::::L                   "\:.   ::.    Jttl
 [:.    :::::::::773.    JE773zs.     I:. ::::.    It3L
;:[     L:::::::::::L    |t::!::J     |::::::::    :Et3
[:L    !::::::::::::L    |t::;z2F    .Et:::.:::.  ::[13
E:.    !::::::::::::L               =Et::::::::!  ::|13
E:.    (::::::::::::L    .......       \:::::::!  ::|i3
[:L    !::::      ::L    |3t::::!3.     ]::::::.  ::[13
!:(     .:::::    ::L    |t::::::3L     |:::::; ::::EE3
 E3.    :::::::::;z5.    Jz;;;z=F.     :E:::::.::::II3[
 Jt1.    :::::::[                    ;z5::::;.::::;3t3
  \z1.::::::::::l......   ..   ;.=ct5::::::/.::::;Et3L
   Rt3.:::::::::::::::J  :E3.  Et::::::::;!:::::;5E3L
    "cz\.:::::::::::::J   E3.  E:::::::z!     ;Zz37`
      \z3.       ::;:::::::::::::::;='      ./355F
        \z3x.         ::~======='         ,c253F
          "tz3=.                      ..c5t32^
             "=zz3==...         ...=t3z13P^
                 `*=zjzczIIII3zzztE3>*^`                           """
    Write.Print(logo, Colors.orange, interval=0)
    wait(0.5)
    d = ''
    print(Colorate.Horizontal(Colors.blue_to_cyan, "\n\n\n[-] Connecting to BTC server", 1),end='\r')
    for i in range(0,4):
        ctypes.windll.kernel32.SetConsoleTitleW('OctoMiner  ||  '+'Connecting to '+whatmining+' Server'+d)
        print(Colorate.Horizontal(Colors.blue_to_cyan, "[-] Connecting to BTC server"+d, 1),end='\r')
        d=d+'.'
        wait(1)
    if internet_on() == True:
        ctypes.windll.kernel32.SetConsoleTitleW('OctoMiner  ||  '+'Connected to '+whatmining+' Server')
        print(Colors.green+"[+] Connected to BTC server     ")
    elif internet_on() == False:
        ctypes.windll.kernel32.SetConsoleTitleW('OctoMiner  ||  '+'Unable connect to '+whatmining+' Server')
        print(Colors.red+"[-] Unable connect to BTC server     ")
        wait(2)
        print(Colors.red+'Check your internet connection')
        ctypes.windll.kernel32.SetConsoleTitleW('OctoMiner')
        wait(1)
        closen()

    wait(3)
    cls()
    alist = ['1','3']
    chars = []
    chars[:0] = string.ascii_letters + string.digits
    ctypes.windll.kernel32.SetConsoleTitleW('OctoMiner  ||  '+whatmining+" | INVALID "+str(invalid)+" | VALID "+str(valid))
    while True:
        lenghte = numpy.random.randint(size=1,low=lowlenght,high=maxlenght)
        c = numpy.random.choice(chars, size=[1,int(lenghte)])
        for s in c:
            wallete = (''.join(x for x in s))
        d = numpy.random.choice(alist, size=[1])
        e = (''.join(x for x in d))
        wallet='bc'+e+wallete
        lenghtofwallet = (len(wallet))
        if loop == 0:
            randbool = numpy.random.randint(size=1,low=randommin,high=randommax)
        if loop == randbool:
            if internet_on() == True:
                        pass
            elif internet_on() == False:
                        ctypes.windll.kernel32.SetConsoleTitleW('OctoMiner  ||  '+'Unable connect to '+whatmining+' Server')
                        print(Colors.red+"[-] Unable connect to BTC server     ")
                        wait(2)
                        print(Colors.red+'Check your internet connection')
                        ctypes.windll.kernel32.SetConsoleTitleW('OctoMiner')
                        wait(1)
                        closen()
            randomofbtc=numpy.random.uniform(0.00001, 0.00094)
            btc4=round(randomofbtc,7)
            try:
                c2onverted=b.convert_btc_to_cur(randomofbtc, 'USD')
                c4=round(c2onverted,2)
            except:
                print('no internet connection')
                c4='x0error'
            if theme == 1:
                if lenghtofwallet == 33:
                    print(Colors.white +"["+Colors.blue+"+"+Colors.white+"] "+wallet+' -> '+Colors.blue+str(btc4)+' BTC ≈ '+str(c4)+' USD')
                elif lenghtofwallet == 32:
                    print(Colors.white +"["+Colors.blue+"+"+Colors.white+"] "+wallet+'  -> '+Colors.blue+str(btc4)+' BTC ≈ '+str(c4)+' USD')
                elif lenghtofwallet == 31:
                    print(Colors.white +"["+Colors.blue+"+"+Colors.white+"] "+wallet+'   -> '+Colors.blue+str(btc4)+' BTC ≈ '+str(c4)+' USD')
                elif lenghtofwallet == 30:
                    print(Colors.white +"["+Colors.blue+"+"+Colors.white+"] "+wallet+'    -> '+Colors.blue+str(btc4)+' BTC ≈ '+str(c4)+' USD')
                elif lenghtofwallet == 29:
                    print(Colors.white +"["+Colors.blue+"+"+Colors.white+"] "+wallet+'     -> '+Colors.blue+str(btc4)+' BTC ≈ '+str(c4)+' USD')
                elif lenghtofwallet == 28:
                    print(Colors.white +"["+Colors.blue+"+"+Colors.white+"] "+wallet+'      -> '+Colors.blue+str(btc4)+' BTC ≈ '+str(c4)+' USD')
                elif lenghtofwallet == 27:
                    print(Colors.white +"["+Colors.blue+"+"+Colors.white+"] "+wallet+'       -> '+Colors.blue+str(btc4)+' BTC ≈ '+str(c4)+' USD')
                elif lenghtofwallet == 26:
                    print(Colors.white +"["+Colors.blue+"+"+Colors.white+"] "+wallet+'        -> '+Colors.blue+str(btc4)+' BTC ≈ '+str(c4)+' USD')
                print(Colors.white+'['+Colors.blue+'!'+Colors.white+'] Wallet found')
                money=money+c4
            elif theme == 2:

                if lenghtofwallet == 33:
                    print(Colors.green + "[+]   Valid || "+Colors.reset+wallet+Colors.green+' ||->'+str(randomofbtc)+' BTC ≈ '+str(c4)+' USD')
                elif lenghtofwallet == 32:
                    print(Colors.green + "[+]   Valid || "+Colors.reset+wallet+Colors.green+'  ||->'+str(randomofbtc)+' BTC ≈ '+str(c4)+' USD')
                elif lenghtofwallet == 31:
                    print(Colors.green + "[+]   Valid || "+Colors.reset+wallet+Colors.green+'   ||->'+str(randomofbtc)+' BTC ≈ '+str(c4)+' USD')
                elif lenghtofwallet == 30:
                    print(Colors.green + "[+]   Valid || "+Colors.reset+wallet+Colors.green+'    ||->'+str(randomofbtc)+' BTC ≈ '+str(c4)+' USD')
                elif lenghtofwallet == 29:
                    print(Colors.green + "[+]   Valid || "+Colors.reset+wallet+Colors.green+'     ||->'+str(randomofbtc)+' BTC ≈ '+str(c4)+' USD')
                elif lenghtofwallet == 28:
                    print(Colors.green + "[+]   Valid || "+Colors.reset+wallet+Colors.green+'      ||->'+str(randomofbtc)+' BTC ≈ '+str(c4)+' USD')
                elif lenghtofwallet == 27:
                    print(Colors.green + "[+]   Valid || "+Colors.reset+wallet+Colors.green+'       ||->'+str(randomofbtc)+' BTC ≈ '+str(c4)+' USD')
                elif lenghtofwallet == 26:
                    print(Colors.green + "[+]   Valid || "+Colors.reset+wallet+Colors.green+'        ||->'+str(randomofbtc)+' BTC ≈ '+str(c4)+' USD')
                print(Colors.green+'[!]'+Colors.white+'   Wallet found')
                money=money+c4
            if saveto  == 2:
                wdir=os.getcwd()
                file_exists = exists(wdir+r"\valid_wallets.txt")
                if file_exists:
                    with open("valid_wallets.txt", "a+") as f:
                        f.write('\n'+wallet+'  ||  '+str(randomofbtc)+' BTC  '+str(c4)+' USD')
                else:
                    with open('valid_wallets.txt', 'w') as f:
                        f.write(wallet+'  ||  '+str(randomofbtc)+' BTC  '+str(c4)+' USD')
                        f.close()
            elif saveto == 1:

                webhook = DiscordWebhook(url=webhooke)
                webhook = DiscordWebhook(url=webhooke, username="OctoHook",avatar_url='https://cdn.discordapp.com/attachments/1031631174415691828/1036005165410549810/octominer.png')
                # create embed object for webhook
                # you can set the color as a decimal (color=242424) or hex (color='03b2f8') number
                embed = DiscordEmbed(title='Valid OctoMiner wallet', description='`'+wallet+'`'+'\n'+str(randomofbtc)+' BTC  '+str(c4)+' USD', color='0000FF')
                # add embed object to webhook
                webhook.add_embed(embed)

                response = webhook.execute()
            elif saveto == 3:
                print('['+Colors.blue+'-'+Colors.white+'] Transfering ' +Colors.blue+str(btc4)+' BTC'+'/'+str(c4)+' USD'+Colors.white+' from '+wallet+Colors.blue+' to '+Colors.white+ywallet)
                wait(1)
                print('['+Colors.blue+'+'+Colors.white+'] Transfer succesful')
            wait(1)



            loop = 0
            valid = valid + 1
            wait(4)


        else:
            if theme == 1:
                if lenghtofwallet == 33:
                    print(Colors.white +"["+Colors.blue+"-"+Colors.white+"] "+Colors.white+wallet+' -> '+Colors.blue+'0.0000000 BTC ≈ 0.00 USD')
                elif lenghtofwallet == 32:
                    print(Colors.white +"["+Colors.blue+"-"+Colors.white+"] "+Colors.white+wallet+'  -> '+Colors.blue+'0.0000000 BTC ≈ 0.00 USD')
                elif lenghtofwallet == 31:
                    print(Colors.white + "["+Colors.blue+"-"+Colors.white+"] "+Colors.white+wallet+'   -> '+Colors.blue+'0.0000000 BTC ≈ 0.00 USD')
                elif lenghtofwallet == 30:
                    print(Colors.white + "["+Colors.blue+"-"+Colors.white+"] "+Colors.white+wallet+'    -> '+Colors.blue+'0.0000000 BTC ≈ 0.00 USD')
                elif lenghtofwallet == 29:
                    print(Colors.white + "["+Colors.blue+"-"+Colors.white+"] "+Colors.white+wallet+'     -> '+Colors.blue+'0.0000000 BTC ≈ 0.00 USD')
                elif lenghtofwallet == 28:
                    print(Colors.white + "["+Colors.blue+"-"+Colors.white+"] "+Colors.white+wallet+'      -> '+Colors.blue+'0.0000000 BTC ≈ 0.00 USD')
                elif lenghtofwallet == 27:
                    print(Colors.white + "["+Colors.blue+"-"+Colors.white+"] "+Colors.white+wallet+'       -> '+Colors.blue+'0.0000000 BTC ≈ 0.00 USD')
                elif lenghtofwallet == 26:
                    print(Colors.white + "["+Colors.blue+"-"+Colors.white+"] "+Colors.white+wallet+'        -> '+Colors.blue+'0.0000000 BTC ≈ 0.00 USD')
            elif theme == 2:

                if lenghtofwallet == 33:
                    print(Colors.red + "[-] Unvalid || "+Colors.reset+wallet+Colors.red+' ||->0.0000000000000000000 BTC ≈ 0.00 USD')
                elif lenghtofwallet == 32:
                    print(Colors.red + "[-] Unvalid || "+Colors.reset+wallet+Colors.red+'  ||->0.0000000000000000000 BTC ≈ 0.00 USD')
                elif lenghtofwallet == 31:
                    print(Colors.red + "[-] Unvalid || "+Colors.reset+wallet+Colors.red+'   ||->0.0000000000000000000 BTC ≈ 0.00 USD')
                elif lenghtofwallet == 30:
                    print(Colors.red + "[-] Unvalid || "+Colors.reset+wallet+Colors.red+'    ||->0.0000000000000000000 BTC ≈ 0.00 USD')
                elif lenghtofwallet == 29:
                    print(Colors.red + "[-] Unvalid || "+Colors.reset+wallet+Colors.red+'     ||->0.0000000000000000000 BTC ≈ 0.00 USD')
                elif lenghtofwallet == 28:
                    print(Colors.red + "[-] Unvalid || "+Colors.reset+wallet+Colors.red+'      ||->0.0000000000000000000 BTC ≈ 0.00 USD')
                elif lenghtofwallet == 27:
                    print(Colors.red + "[-] Unvalid || "+Colors.reset+wallet+Colors.red+'       ||->0.0000000000000000000 BTC ≈ 0.00 USD')
                elif lenghtofwallet == 26:
                    print(Colors.red + "[-] Unvalid || "+Colors.reset+wallet+Colors.red+'        ||->0.0000000000000000000 BTC ≈ 0.00 USD')

            loop = loop + 1
            invalid = invalid + 1
        ctypes.windll.kernel32.SetConsoleTitleW('OctoMiner  ||  '+whatmining+" | UNVALID "+str(invalid)+" | VALID "+str(valid)+" | EARNED "+str(money)+"$")
        if keyboard.is_pressed('space'):
            Write.Input("Paused.\n Press enter to continue.", Colors.red_to_purple, interval=0.0025)

def menui():
    ctypes.windll.kernel32.SetConsoleTitleW('OctoMiner  ||  '+'In Menu')
    global saveto
    global webhooke
    global ywallet
    global bool1
    global bool2
    global theme
    Colors.blue
    title = 'What u want to do?'
    options = ['Mine BTC','Mine BTC Wallets','Transfer BTC','Leave']

    option, index = pick(options, title, indicator='>>', default_index=1)
    if option == 'Transfer BTC':
        ctypes.windll.kernel32.SetConsoleTitleW('OctoMiner  ||  Transfer Menu')
        transfer()
    elif option == 'Mine BTC': pass
    elif option == 'Leave':
        os.exit
    elif option == 'Mine BTC Wallets': pass

    title = 'How to mine?'
    options = ['Hardware','Cloud']

    option, index = pick(options, title, indicator='>>', default_index=1)
    if option == 'Cloud': pass
    elif option == 'Hardware':
        title = 'How to mine?'
        options = ['DRIVE','2FA Keys','CPU','GPU']

        option, index = pick(options, title, indicator='>>', default_index=1)
        if option == 'DRIVE': pass
        elif option == '2FA Keys': pass
        elif option == 'CPU': pass
        elif option == 'GPU': pass
    title = 'what u want to do with wallets? '
    options = ['Send to Discord Webhook','Save to TXT','Transfer to your wallet']
    if dev_version==True:
        options.append('None')
    option, index = pick(options, title, indicator='>>', default_index=1)
    if option == 'Send to Discord Webhook':
        saveto=1
    elif option == 'Save to TXT':
        saveto=2
    elif option == 'Transfer to your wallet':
        saveto=3
    elif option == 'None':
        saveto=4
    if saveto == 1:
        cls()
        cinput('enter Discord Webhook: ')
        webhooke=var
    if saveto == 3:
        while bool1 == False:
            cinput('Enter your wallet:')
            ywallet=var
            if 'bc1' in ywallet or 'bc3' in ywallet and len(ywallet) >= 24 and len(ywallet) <= 31: bool1 = True
            else: print(Colors.red+"Bad Wallet  |  Try again.")
            wait(1)
            cls()
    title = 'Choose Theme'
    options = ['Less info','More info']

    option, index = pick(options, title, indicator='>>', default_index=1)
    if option == 'Less info':
        theme = 1
    if option == 'More info':
        theme = 2
    miner('BTC',24,31,3000,6000)


banner = """
                    ██████████
                  ██░░░░░░░░░░██
                ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓
              ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓
              ██░░▒▒██▒▒▒▒▒▒██▒▒▒▒██
              ██░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
    ██████    ██░░▒▒▒▒▒▒██▒▒▒▒▒▒▒▒██    ██████
  ██████▒▒▓▓    ▓▓▒▒▒▒██▓▓██▒▒▒▒██    ▓▓▒▒████▓▓
██      ██░░██    ██▒▒▒▒██░░▒▒██    ██░░██      ██
██      ██▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▒▒▒▒██      ██
  ██      ██▒▒▒▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒▒▒▒██      ██
            ██▒▒████▒▒▒▒▒▒▒▒▒▒████▒▒██
    ██████    ██░░▒▒██▒▒██▒▒██▒▒▒▒██    ██████
  ██████▒▒████▒▒▒▒██▒▒▒▒██▒▒▒▒██▒▒▒▒████▒▒██████
██      ██▒▒▒▒▒▒██▒▒▒▒██  ██▒▒▒▒██▒▒▒▒▒▒██      ██
██        ██████▒▒████      ████▒▒██████        ██
  ██          ████              ████          ██
            ████                  ████
            ██                      ██
            ██    ██          ██    ██
              ▓▓▓▓              ▓▓▓▓



 ▒█████   ▄████▄  ▄▄▄█████▓ ▒█████   ███▄ ▄███▓ ██▓ ███▄    █ ▓█████  ██▀███
▒██▒  ██▒▒██▀ ▀█  ▓  ██▒ ▓▒▒██▒  ██▒▓██▒▀█▀ ██▒▓██▒ ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
▒██░  ██▒▒▓█    ▄ ▒ ▓██░ ▒░▒██░  ██▒▓██    ▓██░▒██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
▒██   ██░▒▓▓▄ ▄██▒░ ▓██▓ ░ ▒██   ██░▒██    ▒██ ░██░▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄
░ ████▓▒░▒ ▓███▀ ░  ▒██▒ ░ ░ ████▓▒░▒██▒   ░██▒░██░▒██░   ▓██░░▒████▒░██▓ ▒██▒
░ ▒░▒░▒░ ░ ░▒ ▒  ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░   ░  ░░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░ ▒ ▒░   ░  ▒       ░      ░ ▒ ▒░ ░  ░      ░ ▒ ░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
░ ░ ░ ▒  ░          ░      ░ ░ ░ ▒  ░      ░    ▒ ░   ░   ░ ░    ░     ░░   ░
    ░ ░  ░ ░                   ░ ░         ░    ░           ░    ░  ░   ░
         ░


Made By Refil
"""
cls()
try:
        b = BtcConverter()
        converted = b.get_latest_price('USD')
        print('1 BTC = '+ str(converted)+' USD')
except:
        print('no internet connection\n1 BTC = 0xerror')
if dev_version == False:
    Write.Print(banner+'\n\n', Colors.blue_to_cyan, interval=0)

    wait(5)
menui()
