---
title: "Outlook can not connect to exchange server 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1014767/outlook-can-not-connect-to-exchange-server-2016
question_id: 1014767
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Q&A User"]
---
# Outlook can not connect to exchange server 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1014767/outlook-can-not-connect-to-exchange-server-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I have been facing an issue for 1 month. A lot of users in my organization cannot connect outlook. We have an Exchange Server 2016 environment. We checked Outlook 2013, 2016 and 2019 version but issue remains same. We uninstalled outlook and reinstall it but issue still persist. We also checked our virtual directory settings and all are in placed properly. We checked our DNS and its okay. We also tried to disjoined my pc from domain and rejoin it but issue still same. We couldn't connect both internally and externally. Only few users can connect outlook but maximum users failed to connect. So, please suggest me any solution. Thank you.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-21*

First of all check, TLS 1.2, by default, if it is off in Outlook 2016.    

Also, you can check this thread for more help - https://community.spiceworks.com/topic/1723648-outlook-2016-cannot-connect-to-exchange-2016

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-20*

Hi @Md. Rubiat Haque       

See a couple responses on https://social.technet.microsoft.com/Forums/ie/en-US/b8225294-8d03-4ede-b1da-aa3fbce719db/cant-connect-outlook-2016-to-exchange-2016?forum=Exch2016CM (a similar issue with Outlook and Exchange 2016).    

Please use the Microsoft Remote Connectivity Analyzer to run outlook connectivity tests and check if any errors.    

Moreover, I also recommend you refer to the following article and check if any helps:    

Outlook connection issues with Exchange mailboxes because of the RPC encryption requirement    

Outlook: Unable to perform a Check Name or connect to an Exchange mailbox    

(or)    

The fix for me was to edit the authentication settings for the mapi virtual directory in the Exchange Admin center. I enabled Windows Authentication -NTLM, Negotiate and Basic. Outlook clients could then connect and I could proceed with the migration. Hope that helps someone.    

Based on your information this is just a guess at what may help you.    

---------------------------------    

If this is helpful please accept answer.
