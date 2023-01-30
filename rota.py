#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import yaml
import collections
import smtplib
from datetime import datetime


emailsender = ""
jobs = "jobs.example"

with open(jobs,"r") as jobfile:
    data = yaml.safe_load(jobfile)
    emailmessage = f"Subject: Rota {datetime.today().strftime('%Y/%m/%d')}\n\n"
    emailreciever = []
    for k,v in data.items():
        emailmessage += f"{k}: {v[1].upper()}\n"
        emailreciever.append(v[0])
    emailmessage += "\n\nCheers,\nThe Rota"
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(emailsender, emailreciever, emailmessage)
    chores = collections.deque([v[1] for k,v in data.items()])
    chores.rotate()
    new_assignments = data.copy()
    for i,(k,v) in enumerate(data.items()):
        new_assignments[k][1] = chores[i]

with open(jobs,"w") as jobfile:
    yaml.dump(new_assignments,jobfile,default_flow_style=False)
