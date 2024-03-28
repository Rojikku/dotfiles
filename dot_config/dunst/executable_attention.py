#!/usr/bin/env python3
from os import system #Run command for demands_attention
from sys import argv #Import arguments from dunst
import re #Regex Support

# Variables
options = argv
appname = argv[1]
summary = argv[2]
body = argv[3]
command = "wmctrl -r {} -b add,demands_attention".format(appname) # Set demands attention status on calling window

# Debug
# print("Appname: {}\nSummary: {}\nBody: {}".format(appname, summary, body))

def discord():
    mute = re.compile('.*muted', re.IGNORECASE)
    deaf = re.compile('.*deafen', re.IGNORECASE)
    move = re.compile('[A-za-z]+ (joined|left) .*')
    avrae = re.compile('.*Avrae.*')
    sonarr = re.compile('.*Sonarr.*')
    github = re.compile('.*GitHub.*')
    flux = re.compile('.*Flux.*')
    pro = re.compile('.*Prometheus.*')
    exclamation = re.compile('^!.*')

    if mute.match(summary) and body == '': # Ignore mutes
        print("Ignoring mute")
        pass
    elif deaf.match(summary) and body == '': # Ignore deafens
        print("Ignoring deaf")
        pass
    elif move.match(summary) and body == '': # Ignore moves
        print("Ignoring move")
        pass
    elif avrae.match(summary): # Ignore messages from avrae bot
        print("Ignoring avrae")
        pass
    elif exclamation.match(body): # Check body for command
        print("Ignoring !command")
        pass
    elif sonarr.match(summary): # Ignore Sonarr notifs
        print("Ignoring Sonarr")
        pass
    elif github.match(summary):
        print ("Ignoring GitHub")
        pass
    elif flux.match(summary):
        print ("Ignoring Flux")
        pass
    elif pro.match(summary):
        print ("Ignoring Prometheus")
        pass
    else:
        print("Notifying for: {}".format(summary))
        system(command)

if appname == 'discord':
    discord()
else:
    print("Error: No applicable setup!")
