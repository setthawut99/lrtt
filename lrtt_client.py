#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from linepy import LINE, OEPoll
import traceback, sys, time

def jnt(op):

    if op.type == 25:

        if op.message.text == 'hi':
            client.sendMessage(op.message.to, 'Hi too !! How are you ?')
        if op.message.text == "sp":
            st = time.time()
            client.getProfile()
            client.sendMessage(op.message.to, "%s" % (time.time() - st))

client = LINE()
oepoll = OEPoll(client)
print(client.authToken)

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops:
            for op in ops:
                try:
                    jnt(op)
                except Exception:
                    traceback.print_exc()
                oepoll.setRevision(op.revision)
    except Exception:
        traceback.print_exc()
        exit()
    except KeyboardInterrupt:
        sys.exit(1)