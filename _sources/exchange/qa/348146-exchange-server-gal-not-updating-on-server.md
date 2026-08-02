---
title: "Exchange Server GAL not updating on server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/348146/exchange-server-gal-not-updating-on-server
question_id: 348146
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange Server GAL not updating on server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/348146/exchange-server-gal-not-updating-on-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have noticed that on my Exchange 2016 server GAL contains old entries and will not update. I have gone into the Organization in the Exchange admin center and forced an update, but it still says Not up to date. I have tried the Management shell to update, looks like it updates but it does not. I have tried about everything on the internet to no avail.   

Any suggestions?  

Thanks,

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2021-04-08*

Hi, @Gray, Jeff       

May I ask what solutions have you tried so far?    

I have gone into the Organization in the Exchange admin center and forced an update, but it still says Not up to date. I have tried the Management shell to update, looks like it updates but it does not.     

To update a GAL, you need to use Exchange Management Shell. It cannot be processed via Exchange Admin Center.    

Did you run the command Update-GlobalAddressList -Identity <GAL name>?    

I noticed that you mentioned the GAL still contains old entries, can you see the old entries via "Preview recipients the global address list includes" in EAC?    

    

If so,please check if there are some AD replication latency in the environment.    

If the entries only show on Outlook clients, the issue may be due to the Offline Address Book is not up to date.    

Please run the Update-OfflineAddressBook -Identity <OAB name> command via Exchange Management Shell.    

And then manually download OAB via Outlook client:    

Send/Receive > Send/Receive Groups > Download Address Book    

You may also test with Outlook online mode to check if the old entries are excluded in the address book.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
