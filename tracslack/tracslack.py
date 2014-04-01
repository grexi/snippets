#!/usr/bin/python

# Send Trac ticket updates to Slack
# 
# Written by Gregor Dorfbauer / gd@usersnap.com
# http://usersnap.com - Show, don't tell.
#
#
# Setup Steps: 
# update your trac.ini
# ####################
# [notification]
# smtp_always_cc = slack@localhost
# ####################
# invoke with a .forward file of your slack user - content "|/home/slack/tracslack.py"

import sys
import json
import requests
import email
import base64

LOGFILE="/home/slack/log.txt"
SLACK_URL="https://yourcompany.slack.com/services/hooks/incoming-webhook"
SLACK_TOKEN="ABc293jBlPyktTIasdagasd"

#those are free to choose
SLACK_CHANNEL="#trac"
SLACK_USERNAME="trac"
SLACK_EMOJI=":rocket:"


###############################################################################
ofile = open(LOGFILE, "a")

firstempty = False
subject = ""
content = email.message_from_string(sys.stdin.read())
payload = content.get_payload()
try:
    payload = base64.decodestring(payload)
except:
    pass
newcont = []
omitheader = 2
ofile.write("Payload: %r" % payload)
for line in payload.split("\n"):
    ofile.write("line %r" % line)
    #filter out header + lines (free to extend)
    if omitheader == 2 and "-----+-----" in line: 
       omitheader -= 1
       continue
    if omitheader == 1:
       if "-----+-----" in line:
           omitheader -= 1
       continue
    if line in ("-- ", ""):
       continue
    newcont.append(line)

ofile.write("newcont: %r" % newcont)

data = {"channel": SLACK_CHANNEL,
        "username": SLACK_USERNAME,
        "text": "%s"% ("\n".join(newcont)),
        "icon_emoji": SLACK_EMOJI
      }
ofile.write("got mail\n")
ofile.write(json.dumps(data,indent=2))
r = requests.post(SLACK_URL, data={"token": SLACK_TOKEN, "payload":json.dumps(data)})
ofile.write("r.status %r r.text %r " % (r.status_code, r))
ofile.write("\n\n")


