---
title: "Monitor ADFS User logon / logoff events to federated applications"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/8347/monitor-adfs-user-logon-logoff-events-to-federated
question_id: 8347
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Monitor ADFS User logon / logoff events to federated applications

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/8347/monitor-adfs-user-logon-logoff-events-to-federated (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Thanks in advance  

I need to audit user logon and logs offs on our applications that use ADFS for federation, but I cannot seems to find any information on how to manage this. here is what I need to do, if a user logs on to one of our applications federated through ADFS we need to log the username, application and time. the application can just point to the trust assigned to the application we can correlate it from there.  

if someone know of a good resource on how to accomplish this it would greatly be appreciated.

## Answer (community) — community member

*upvotes: 1 · updated: 2020-11-05*

I also had this question.     

My result is a CSV file with all the logon and sign-out activity (and other useful stuff).    

In Eventlog you can rightclick on an event and set "Attach Task to this event".  This creates a special scheduled task that will only be triggered when that specific event occurs. In that scheduled task, I start a VBS script that looks for the first event in the Eventlog for that event number. And the result I write in a log file.    

The following events are useful on ADFS : 1200,1201,1203,1206,1210    

The structure of the event (XML) is for the above events all the same, so the script can be used for all 12xx events. So I make use of an argument (which is the number of the event) in the scheduled task that is consumed by my VBS script.    

Its very usefull, because I also send an email for some major problems, or when an account is locked by ADFS with Smartlock.    

On the WAP server I did the same but for other events: 14027,14032,13015,12025,13046,245,396,224    

I shared my VBS code in this post.37716-readeventlogsvbs.txt    

I took the part of my ADFS documentation (about logging) and attached it to this post. PS.: The VBS script is not finished yet completely. For example, in the script you'll find the log file name and location. You must create an empty log file first with the correct name D:\logging\logs\secruitylog.csv37791-logging-and-alerting.pdf    

The scheduled task must run with a user that has specific rights. If you want, I can give you more specifications about that too.37781-readeventlogsvbs.txt

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-03-28*

The audit configuration depends of the version of your ADFS farm.    

This is a good starting point: https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/troubleshooting/ad-fs-tshoot-logging
