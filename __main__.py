# Filename : <tahm1d>
# Python Bytecode : 2.7
# Time Succses Decompiled : Wed Sep  9 14:43:39 2020
# Timestamp In Code : 2020-09-02 17:33:14

import sys, random
from os import system
from time import sleep
try:
    import requests
except ImportError:
    system('python2 crack.py')

try:
    request = requests.get('https://www.google.com/search?q=tahmid+rayat', timeout=3)
except (requests.ConnectionError, requests.Timeout) as exception:
    print '\x1b[1;91m[\x1b[1;96m!\x1b[1;91m]\x1b[1;93m No internet connection \x1b[1;91m[\x1b[1;96m!\x1b[1;91m]\x1b[1;97m'
    sys.exit()

try:
    from crkpk import cra3kmenu
except ImportError:
    system('python2 crack.py')

logo = '\n\x1b[1;93m    ___  ____ _  _  \x1b[1;92m  ____ ____ _  _ \n\x1b[1;93m    |__] |__| |_/   \x1b[1;92m  |    |__/ |_/  \n\x1b[1;93m    |    |  | | \\_   \x1b[1;92m |___ |  \\ | \\_ \n\n\x1b[1;96m    Pakistani Facebook Account Cloner\n \x1b[1;97m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n \x1b[1;97m\xe2\x95\x91  \x1b[1;92mAuthor     \x1b[1;96m:\x1b[1;93m   ETHC-404 \x1b[1;97m|\x1b[1;93m Arbab Memon  \x1b[1;97m\xe2\x95\x91\n \x1b[1;97m\xe2\x95\x91  \x1b[1;92mGithub     \x1b[1;96m:\x1b[1;93m   github.com/ETHC-404     \x1b[1;97m\xe2\x95\x91\n \x1b[1;97m\xe2\x95\x91  \x1b[1;92mFacebook   \x1b[1;96m:\x1b[1;93m   arbab.memon.official   \x1b[1;97m\xe2\x95\x91\n \x1b[1;97m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n'

def htrprint(s):
    for t in s + '\n':
        sys.stdout.write(t)
        sys.stdout.flush()
        sleep(0.01)


usercode = requests.get('https://pastebin.com/raw/09VREP6V')
userxx = usercode.text
passcode = requests.get('https://pastebin.com/raw/MiEXvv2U')
passxx = passcode.text
haxuser = userxx
haxpwd = passxx
__ = ['\x1b[1;31m', '\x1b[1;32m', '\x1b[1;34m', '\x1b[1;36m']

def hload():
    loader = ['\xe2\x97\x8f   ', '\xe2\x97\x8f\xe2\x97\x8f   ', '\xe2\x97\x8f   ', '\xe2\x97\x8f\xe2\x97\x8f   ', '\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f   ', '\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f   ']
    for Z in loader:
        sys.stdout.write('\t\r%s[%s\xf0\x9d\x95\xb3\xf0\x9d\x95\xbf\xf0\x9d\x95\xbd%s]%s Logging in %s' % (random.choice(__), random.choice(__), random.choice(__), random.choice(__), random.choice(__)) + Z)
        sys.stdout.flush()
        sleep(1)

    print '%s[%sSUCCEED%s]' % ('\x1b[1;32m', random.choice(__), '\x1b[1;32m')


def log():
    system('clear')
    print logo
    print '\x1b[1;92mINPUT USERNAME & PASSWORD\x1b[0m'
    print '\x1b[1;96m-------------------------\x1b[0m'
    print ''
    usr = raw_input('\x1b[1;93m          INPUT USERNAME \x1b[1;96m:\x1b[1;92m ')
    if usr == haxuser:
        fog()
    else:
        system('clear')
        system('pip2 install crkpk --upgrade > /dev/null 2>&1 &')
        print logo
        print '\x1b[1;92mINPUT USERNAME & PASSWORD\x1b[0m'
        print '\x1b[1;96m-------------------------\x1b[0m'
        print ''
        print '\x1b[1;93m          TOOL USERNAME \x1b[1;96m:\x1b[1;97m ' + usr + ' \x1b[1;91m[wrong]\x1b[0m'
        sleep(1)
        system('xdg-open https://github.com/htr-tech')
        log()


def fog():
    system('clear')
    print logo
    print '\x1b[1;92mINPUT USERNAME & PASSWORD\x1b[0m'
    print '\x1b[1;96m-------------------------\x1b[0m'
    print ''
    print '\x1b[1;93m          INPUT USERNAME \x1b[1;96m:\x1b[1;97m ARBAB MEMON \x1b[1;92m[correct]\x1b[0m'
    pwd = raw_input('\n\x1b[1;93m          INPUT PASSWORD \x1b[1;96m:\x1b[1;92m ')
    if pwd == haxpwd:
        dog()
    else:
        system('clear')
        system('pip2 install crkpk --upgrade > /dev/null 2>&1 &')
        print logo
        print '\x1b[1;92mINPUT USERNAME & PASSWORD\x1b[0m'
        print '\x1b[1;96m-------------------------\x1b[0m'
        print ''
        print '\x1b[1;93m          TOOL USERNAME \x1b[1;96m:\x1b[1;97m ARBAB MEMON \x1b[1;92m[correct]\x1b[0m'
        print '\n\x1b[1;93m          TOOL PASSWORD \x1b[1;96m:\x1b[1;97m ' + pwd + ' \x1b[1;91m[wrong]\x1b[0m'
        sleep(1)
        system('xdg-open https://linktr.ee/tahmid.rayat')
        fog()


def dog():
    system('clear')
    print logo
    print '\x1b[1;92mINPUT USERNAME & PASSWORD\x1b[0m'
    print '\x1b[1;96m-------------------------\x1b[0m'
    print ''
    print '\x1b[1;93m          TOOL USERNAME \x1b[1;96m:\x1b[1;97m ARBAB MEMON \x1b[1;92m[correct]\x1b[0m'
    print '\n\x1b[1;93m          TOOL PASSWORD \x1b[1;96m:\x1b[1;97m ETHICAL-404 \x1b[1;92m[correct]\x1b[0m'
    print ''
    hload()
    cra3kmenu()


if __name__ == '__main__':
    system('rm -rf *.pyc *.dis')
    log()
