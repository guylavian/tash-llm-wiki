---
title: "PST File reach to 120 GB in Microsoft Exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1599664/pst-file-reach-to-120-gb-in-microsoft-exchange-201
question_id: 1599664
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# PST File reach to 120 GB in Microsoft Exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1599664/pst-file-reach-to-120-gb-in-microsoft-exchange-201 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,
I am using Microsoft Exchange 2019 Version 15.2 ‎(Build 986.5)‎ Enterprise, One of my user mail file increases and reach to 110GB, as emails of users are very important to us, previously I change default quota of email to customized and set limit of 180 GB on EAC, Since the mail file is increasing, Is there any solution other than compacting, to reduce size of pst file on both server and client end (Microsoft 2013), is there authentic tool, recommended by Microsoft to handle this issue, as so much tools are available to compact the files but I don't know which should be risk free and authentic. or any solution offered by Microsoft ?
Thank you

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-02-28*

Hi @Farrukh Ali Qureshi  ，  

I read through your post but got a little confused about your concern. PST file is a type of Outlook data file which is usually used by POP3 account, see this article for more details. While from your description like "change default quota of email to customized and set limit of 180 GB on EAC" , are you actually talking about the mailbox size as displayed in images below?  

If so, on the one hand, from the perspective of the end-user's side, there are several methods and best practices to manage the mailbox size from Outlook client:  

Manage my mailbox size  

On the other hand, as the Exchange administrator, you can consider enabling the archive mailbox for this user so that the user can store messages in an archive mailbox, which is accessible by using Outlook or OWA. See Manage In-Place Archives in Exchange Server. Besides, you could also create and then apply a retention policy to the user based on your needs, it's a common practice in the field of Exchange that can help keep users' mailbox size under control. For more information, hopefully you can find this document helpful: Create a retention policy in Exchange Server.  

Feel free to let me know if I have misunderstood anything.  

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
