---
title: "Microsoft Exchange 2019 mailbox message behavior in cache mode"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1129674/microsoft-exchange-2019-mailbox-message-behavior-i
question_id: 1129674
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Microsoft Exchange 2019 mailbox message behavior in cache mode

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1129674/microsoft-exchange-2019-mailbox-message-behavior-i (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Sir,    

```
I am simulating a Exchange DR rollback condition, I have a question in Exchange 2019 mailbox behavior with Outlook cache mode after server rollback. It seems that it is different with what I learn.
```

Environemnt:    

Exchange Server1 (Ex2019): Mailbox user1    

Outlook  2016/2019: Connect to user1 mailbox with cache mode    

I take a snapshot of Exchange 2019 Server at e.g. (time: 12:00 pm), then I use Outlook "User1" to connect mailbox:    

When Outlook connect to Exchange of user1 mailbox box, user1 has 3 folders message:    

-  Inbox folder : Message 1 ,2    

-  New Folder created called: "Folder1" : It has message 3 inside    

-  Send folder :  Message 4,5    

After operation, the server time is 12:30 pm, I shutdown Ex2019 server and rollback Ex2019 Server snapshot to 12:00pm.     

When 12:00 version of Ex2019 server start up, I use PC OWA to connect:    

The mailbox message will show in Ex2019 OWA:    

-   Inbox : No message,     

-  Folder A, no created    

-  Sent item : No message.    

Yes, it is correct behaviour.    

When I use the 12:30 version of PC outlook to connect 12:00 pm version of Exchange Server, and also press the update all folder button.    

The PC Outlook will show:    

-  Inbox:  Message 1,2, still there    

-  Folder A missed    

-  Sent item folder in Outlook: Message 4,5 still there.    

When I use the OWA to see after PC outlook connected:    

-  Inbox: Empty no message    

-  Folder A missed    

-  Sent Item folder: Empty no message    

Question:     

-  Previously, I understand that server mailbox user1 (12:00pm verion) will sync to PC outlook message which cause Inbox & Sent Item folder message empty, Actually, it seems no empty of message.    

-  It can remove the "Folder A" after PC outlook connected.    

Why it has such behaviour when new update of Outlook cache mode client to connect rollback of Exchange Server user mailbox?    

Anyone has idea on it?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-16*

@JOE TAM      

Because the Outlook Cache will use the local OST file first, it need time to sync with server side and update folder.    

You could try to recreate a new profile after recover Exchange server. It will show the correct data.    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
