---
title: "Exchange 2016 EMS stopped working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/390821/exchange-2016-ems-stopped-working
question_id: 390821
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016 EMS stopped working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/390821/exchange-2016-ems-stopped-working (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

We had a failed Exchange 2016 server and decided to build a new one.    

Fresh Server 2016 install with Exchange 2016 CU20.    

After having a lot of trouble moving (read: create a new database on the new server, copy the old database to the new server and create a recovery database using the old database, move everything from the recovery database to the new database)  the database via EMS we are now having issues with EMS, it just won't start anymore and shows below error:    

    

I have checked the time on the server, it's correct.    

SSL certificate seems to be fine as well.    

WinRM seems to be fine and the needed services are running.    

What could be wrong here?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-12*

It seems like the failing mail delivery and the EMS failing was caused by the failed Exchange server (still didn't figure out how but oh well...).  

After I shut the failing Exchange server down I could connect to the EMS of the new server.  

Removed everything from the old server using EMS (the VD's) and removed all the connectors for the old server in ECP.  

After that I disjoint the domain and removed all the DNS records pointing to the old server and removed it's AD account.  

I then followed this guide (https://techgenix.com/removing-exchange-server-mailbox-your-environment/#:~:text=When%20removing%20a%20server%20that,on%20Uninstall%20(Item%202).) from the section Removing manually... using ADSI Edit.  

As last step I removed the databases from the old in ADSI Edit as well.  

Leaving this open for a little while in case it goes wrong again :)

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-12*

SMTP error is back as well :(  

SMTP error from remote mail server after end of data: host 192.168.200.45 [192.168.200.45]: 451 4.7.0 Temporary server error. Please try again later. PRX4

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-12*

Great.    

Have you tried re-creating the powershell VD?    

1 Open windows powershell and run add-pssnapin Microsoft.Exchange.Management.PowerShell.SnapIn    

2 Remove the VD:    

```
Get-PowerShellVirtualDirectory -Server | Remove-PowerShellVirtualDirectory
```

3 Create the VD:    

```
New-PowerShellVirtualDirectory -Server  -Name Powershell -RequireSSL $false -BasicAuthentication $false -WindowsAuthentication $false -InternalUrl http:///powershell
```

4 Run IISreset.    

Also, check if any errors in Event log.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-11*

Also after a reboot, emails cannot be delivered anymore with following error message:  

SMTP error from remote mail server after end of data: host 192.168.200.45 [192.168.200.45]: 451 4.7.0 Temporary server error. Please try again later. PRX4
