---
title: "Exchange 2019, problem sending email from all clients"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/203398/exchange-2019-problem-sending-email-from-all-clien
question_id: 203398
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2019, problem sending email from all clients

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/203398/exchange-2019-problem-sending-email-from-all-clien (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I'm stuck with a strange problem for days now.  

Last month i installed a fresh 2019 echange on premise server.  

After installation, got the mailflow working, tested it form phone and owa, all works fine.  

2 days ago i was beginning with the preparation of the migration for the cient from hosted exchange to this new own exchange server.  

After creating en few mailboxes, i wanted to test send mail from shared mailbox to see if the sended mail lands in the send items of the shared mailbox, but i noticed an delay on sending emails.  

It seems like exchange itself has some problems, but i cant figure out what it is.  

Remote connectivity en outlook anywhere connectivity test are all OK, eventlogs doenst show any strange things, queu's are empty.  

What are the symptons ?  

Outlook 2019 in normal mode :  

Can connect to server, see all mail, can click around with no delay. But after composing an e-mail, and clicking on send, outlook freezes, showing  non responding with white bars , and after 1-2 minutes outlook reacts again, and mail is send.  

Outlook 2019 in Cached mode.  

Can connect to server, see all mail, can click around with no delay. But after composing an e-mail, and clicking on send,   

the status bar in the bottom of outlook showing an "sending email'status for 1-2 minutes.  

send email is not visible anywhere,  but after the 1-2 minutes is shows in send items.  

Mail on Android phone.  

Can connect, browse folders, but after composing and sending an email it loads for 1-2 minutes, and then the message is send.  

OWA in a browser.  

Can connect to the mailbox, can browse. But after composing an mail an clicking on send, its seems like its send.  

But not visible in any folder, after 2 minutes it shows up in send items.  

OWA in browser on an android phone.  

Can login, browse folders, but when sending an mail, it shows the status 'Busy sending email" for about 1-2 minutes, after that its sended.  

At first i thought it was the spam filter, so routed outgoing mail directly, but that give no difference.  

Outlook anywhere and Autodicsover is configured correctly,  

adding an account in e.g outlook takes only few seconds providing name, email and password.  

Sending an mail on 09:00 is recieved at the other end 3 ore 4 minutes later,   

this is for internal, and external mail.  

Incomming mails has a delay of 1 minutes, but thats because of spam filtering, and no problem.  

The greatest probem is freezing/not responding outlook/owa/android client.  

There were no changes on the system between installation, and start migration.  

Only added an few accepted maildomains and created an email policy specific for one OU.  

I do think the problem is on the server itself, because all clienst have the same problem, only when clicking on send.  

Please Advice !

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-31*

i think i made an error posting the first post, dont know the account anymore, so i cannot mark the answer...  

Please do it for me

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-29*

Problem is found,   

It was an faulty change in dns settings done by a colleguea who didnt log his change.  

So there was an error in the internal record, changed that and flow is constant and direct again.  

Strange that you cant find something like that in the logs.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-21*

Hi @Steve de M   ,    

According to the information you provided, you can successfully configure Outlook, send and receive emails, and the Event log and Queue are normal. Then I think the settings of your Exchange organization are correct.    

According to the message tracking log you provide, the delay time is generated after "Submit"( This event represents: The Mailbox Transport Submission service successfully transmitted the message to the Transport service.) In the transport service, mail recipient analysis, routing analysis, content conversion and other operations will be performed. This will delay the delivery of the mail, which is normal. Exchange 2019 has higher requirements for hardware, especially memory requirements, which are greatly improved compared to the previous version. So please check Microsoft's system requirements for Exchange 2019 first. If the recommended configuration is not reached, then I recommend that you improve your system configuration to speed up email processing.    

For more information:  Exchange Server system requirements and mail-flow    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-18*

Message tracking of an internal mail, send form one user to another on the same exchange. :  

You see the delay of 3 minutes between 11:01 and 11:04  (server name is anonymised)  

Ingediend  

18-12-2020 11:01 SERVER01  

Het bericht werd verzonden naar server01.domain.local.  

In behandeling  

18-12-2020 11:01 server01.domain.local  

Bericht ontvangen door server01.domain.local.van server01.domain.local  

18-12-2020 11:04 server01.domain.local  

Het bericht werd overgebracht van server01.domain.local naar server01.domain.local  

Afgeleverd  

18-12-2020 11:04 server01.domain.local  

Het bericht werd met succes bezorgd.
